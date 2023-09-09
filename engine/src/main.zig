const std = @import("std");
const clamav = @cImport({
	@cInclude("clamav.h");
});

pub fn main() !void {
    const stdout = std.io.getStdOut().writer();

    // Try loading the C functions from ClamAV
    var cg_init_status:c_uint = clamav.cl_init(clamav.CL_INIT_DEFAULT);

	// Check the cg_init_status
	if(cg_init_status == clamav.CL_SUCCESS){
    		try stdout.print("SUCCESSFULLY INITIALIZED LIBCLAMAV\n", .{});
	}
	else{
    		try stdout.print("FAILED TO INITIALIZE LIBCLAMAV\n", .{});
	}

}
