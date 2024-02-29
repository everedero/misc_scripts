# Invoke from shell with
#(gdb) source script_gdb.cmd
set $ram_size = 65536
set $max_iter = 100

define dltrace
	echo Trace retrieval script\n
	# Delete breakpoints
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
end
document dltrace
	Download trace from device\n
end
