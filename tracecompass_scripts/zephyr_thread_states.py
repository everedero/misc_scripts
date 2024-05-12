#
# This script is meant to be run on Trace Compass with EASE scripting module.
#

loadModule('/TraceCompass/Trace')
loadModule('/TraceCompass/Analysis')
loadModule('/TraceCompass/DataProvider')
loadModule('/TraceCompass/View')
loadModule('/TraceCompass/Utils')

def runAnalysis(ss):
    ticker_quark = ss.getQuarkAbsoluteAndAdd('interrupt')
    tasks = {}
    current_running_task = None

    itera = analysis.getEventIterator()
    while itera.hasNext():
        event = itera.next()
        event_name = event.getName()
        event_ts = event.getTimestamp().toNanos()

        if event_name == "isr_enter":
            ss.modifyAttribute(event_ts, "IRQ", ticker_quark)

        if event_name == "isr_exit":
            ss.modifyAttribute(event_ts, "", ticker_quark)


        if event_name == "thread_create":
            task_name = getEventFieldValue(event, "name")
            task_identifier = getEventFieldValue(event, "thread_id")
            print(task_identifier)

            task = {
                "name": task_name,
                "identifier": task_identifier,
                "stack_start": 0,
                "stack_size": 0,
                "priority": 0,
                "state": "Ready",
                "quark": 0,
            }
            if task_name != "unknown":
                task["quark"] = ss.getQuarkAbsoluteAndAdd('[ thread ] ' + \
                        task["name"])
                ss.modifyAttribute(event_ts, task["state"], task["quark"])

            tasks[task["identifier"]] = task


        if event_name == "thread_info":
            task_identifier = getEventFieldValue(event, "thread_id")
            task = tasks[task_identifier]
            task["stack_start"] = getEventFieldValue(event, "stack_base")
            task["stack_size"] = getEventFieldValue(event, "stack_size")


        if event_name == "thread_priority_set":
            task_identifier = getEventFieldValue(event, "thread_id")
            task = tasks[task_identifier]
            task["priority"] = getEventFieldValue(event, "prio")


        if event_name == "thread_name_set":
            task_identifier = getEventFieldValue(event, "thread_id")
            task = tasks[task_identifier]
            task["name"] = getEventFieldValue(event, "name")
            task["quark"] = ss.getQuarkAbsoluteAndAdd('[ thread ] ' + \
                    task["name"])

            ss.modifyAttribute(event_ts, task["name"], task["quark"])


        if event_name == "moved_task_to_ready_state":
            task_identifier = getEventFieldValue(event, "thread_id")
            task = tasks[task_identifier]
            task["state"] = "Ready"

            ss.modifyAttribute(event_ts, task["state"], task["quark"])


        if event_name == "thread_switched_out"or event_name == "thread_pending":
            task_identifier = getEventFieldValue(event, "thread_id")
            if task_identifier not in tasks.keys():
                print("Nullnull")
                continue

            task = tasks[task_identifier]
            ss.modifyAttribute(event_ts, "Ready", task["quark"])


        if event_name == "thread_switched_in"or event_name == "thread_resume" :
            task_identifier = getEventFieldValue(event, "thread_id")
            if task_identifier not in tasks.keys():
                print("Nullnull2")
                continue

            current_running_task = task;
            name = getEventFieldValue(event, "name")
            ss.modifyAttribute(event_ts, "Running", task["quark"])

        if event_name == "thread_suspend"or event_name == "thread_abort":
            task_identifier = getEventFieldValue(event, "thread_id")
            task = current_running_task
            task["state"] = "Blocked"

            quark = tasks[task["identifier"]]
            ss.modifyAttribute(event_ts, task["state"], task["quark"])

    if event != None:
        ss.closeHistory(event.getTimestamp().toNanos())

# Get the active trace
trace = getActiveTrace()

# Get an analysis
analysis = createScriptedAnalysis(trace, "ringTimeLine.js")

ss = analysis.getStateSystem(False)
if not ss.waitUntilBuilt(0):
    runAnalysis(ss)

hmap = java.util.HashMap()
hmap.put(ENTRY_PATH, '*')
provider = createTimeGraphProvider(analysis, hmap)
if provider != None:
    openTimeGraphView(provider)
