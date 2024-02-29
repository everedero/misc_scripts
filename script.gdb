# Invoke from shell with
# (gdb) source script_gdb.cmd
# Then use dltrace and tracebetween as custom user commands

set $ram_size = 65536
set $max_iter = 100

define dltrace
	echo Trace retrieval script\n
	# Delete existing breakpoints
	delete all
	set $i = 0
	# Break when buffer full
	break tracing_backend_ram.c:27

	# Loop for a while
	while ($i < $max_iter)
		printf "Iteration %d\n", $i
		continue
		# Dump ram memory in a file
		eval "dump binary memory data/channel%d ram_tracing ram_tracing+%d", $i, $ram_size
		# Resetting variables
		set variable pos=0
		set variable buffer_full=0
		set $i = $i+1
	end
	# Cleanup breakpoints
	delete all
end
document dltrace
	Download trace from device\n
end

# Takes two arguments, testpoint 1 and testpoint2
# (gdb) tracebetween main.c:331 main.c:333
define tracebetween
	echo Trace retrieval script\n
	# Delete existing breakpoints
	delete all
	break $arg0
	continue
	# Resetting variables
	set variable pos=0
	set variable buffer_full=0
	# Remove first testpoint and add second
	delete all
	break $arg1
	continue
	# Dump ram memory in a file
	set $i = 0
	if $buffer_full
		printf Buffer full before reaching second testpoint
	end
	eval "dump binary memory data/channelb%d ram_tracing ram_tracing+%d", $i, $ram_size
end
document tracebetween
	Download trace from device between two testpoints\n
end
