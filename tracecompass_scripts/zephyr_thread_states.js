/*
 * This script is meant to be run on Trace Compass with EASE scripting module.
 */

loadModule('/TraceCompass/Trace')
loadModule('/TraceCompass/Analysis');
loadModule('/TraceCompass/DataProvider');
loadModule('/TraceCompass/View');
loadModule('/TraceCompass/Utils');

function runAnalysis(ss) {
    var ticker_quark = ss.getQuarkAbsoluteAndAdd('interrupt');
    var tasks = {};
    var current_running_task = null;

    var iter = analysis.getEventIterator();
    while (iter.hasNext()) {
        event = iter.next();
        event_name = event.getName();
        event_ts = event.getTimestamp().toNanos();

        if (event_name == "isr_enter") {
            ss.modifyAttribute(event_ts, "IRQ", ticker_quark);
        }
        if (event_name == "isr_exit") {
            ss.modifyAttribute(event_ts, "", ticker_quark);
        }

        if (event_name == "thread_create") {
            task_name = getEventFieldValue(event, "name");
            task_identifier = getEventFieldValue(event, "thread_id");
            print(task_identifier);

            task = {
                name: task_name,
                identifier: task_identifier,
                stack_start: 0,
                stack_size: 0,       
                priority: 0,
                state: "Ready",
                quark: 0,
            }
            if (task_name != "unknown") {
			    task.quark = ss.getQuarkAbsoluteAndAdd('[ thread ] ' + task.name);
                ss.modifyAttribute(event_ts, task.state, task.quark);
            }
			tasks[task.identifier] = task;

        }
        if (event_name == "thread_info") {
            task_identifier = getEventFieldValue(event, "thread_id");
            task = tasks[task_identifier];
            task.stack_start = getEventFieldValue(event, "stack_base");
            task.stack_size = getEventFieldValue(event, "stack_size");
        }
        
        if (event_name == "thread_priority_set") {
            task_identifier = getEventFieldValue(event, "thread_id");
            task = tasks[task_identifier];
            task.priority = getEventFieldValue(event, "prio");
        }
        
        if (event_name == "thread_name_set") {
            task_identifier = getEventFieldValue(event, "thread_id");
            task = tasks[task_identifier];
            task.name = getEventFieldValue(event, "name");
            task.quark = ss.getQuarkAbsoluteAndAdd('[ thread ] ' + task.name);

            ss.modifyAttribute(event_ts, task.name, task.quark);
        }

        if (event_name == "moved_task_to_ready_state") {
            task_identifier = getEventFieldValue(event, "thread_id");
            task = tasks[task_identifier];
            task.state = "Ready";

            ss.modifyAttribute(event_ts, task.state, task.quark);
        }

        if (event_name == "thread_switched_out" || event_name == "thread_pending") {
            task_identifier = getEventFieldValue(event, "thread_id");
            task = tasks[task_identifier];
            if (task == null) {
                print("Nullnull");
                continue;
            }
            task = tasks[task_identifier];
            ss.modifyAttribute(event_ts, "Ready", task.quark);
        }

        if (event_name == "thread_switched_in" || event_name == "thread_resume" ) {
            task_identifier = getEventFieldValue(event, "thread_id");
            task = tasks[task_identifier];
            if (task == null) {
                // Need to be able to create task on the fly
                continue;
            }
            current_running_task = task;     
            name = getEventFieldValue(event, "name");
            ss.modifyAttribute(event_ts, "Running", task.quark);
        }

        if (event_name == "thread_suspend" || event_name == "thread_abort") {
            task_identifier = getEventFieldValue(event, "thread_id");
            task = current_running_task;
            task.state = "Blocked";

            quark = tasks[task.identifier];
            ss.modifyAttribute(event_ts, task.state, task.quark);
        }
    }

    if (event != null) {
        ss.closeHistory(event.getTimestamp().toNanos());
    }
}


// Get the active trace
var trace = getActiveTrace()

//Get an analysis
var analysis = createScriptedAnalysis(trace, "ringTimeLine.js")

var ss = analysis.getStateSystem(false);
if (!ss.waitUntilBuilt(0)) {
    runAnalysis(ss);
}

var map = new java.util.HashMap();
map.put(ENTRY_PATH, '*');
provider = createTimeGraphProvider(analysis, map);
if (provider != null) {
    openTimeGraphView(provider);
}
