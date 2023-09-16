const std = @import("std");
const buildin = @import("builtin");
const unicode = std.unicode;
const tag = buildin.os.tag;
const join = std.fs.path.join;

// Although this function looks imperative, note that its job is to
// declaratively construct a build graph that will be executed by an external
// runner.
pub fn build(b: *std.Build) void {
    // Standard target options allows the person running `zig build` to choose
    // what target to build for. Here we do not override the defaults, which
    // means any target is allowed, and the default is native. Other options
    // for restricting supported target set are available.
    const target = b.standardTargetOptions(.{});

    // Standard optimization options allow the person running `zig build` to select
    // between Debug, ReleaseSafe, ReleaseFast, and ReleaseSmall. Here we do not
    // set a preferred release mode, allowing the user to decide how to optimize.
    const optimize = b.standardOptimizeOption(.{});

    const exe = b.addExecutable(.{
        .name = "engine",
        // In this case the main source file is merely a path, however, in more
        // complicated build scripts, this could be a generated file.
        .root_source_file = .{ .path = "src/main.zig" },
        .target = target,
        .optimize = optimize,
    });
    switch (tag) {
        .windows => {
            const clamav_path = b.env_map.get("CLAMAV_DIR") orelse "C:\\clamav";
            std.debug.print("clamav path is {s}\n", .{clamav_path});
            const clamav_include_raw = std.fmt.allocPrint(b.allocator, "{s}\\include", .{clamav_path});
            const clamav_include = clamav_include_raw catch "C:\\clamav\\include";
            defer b.allocator.free(clamav_include);

            exe.addIncludePath(clamav_include);
            exe.addLibraryPath(clamav_path);

            const openssl_path = b.env_map.get("OPENSSLDIR") orelse "C:\\openssl";
            std.debug.print("openssl path is {s}\n", .{openssl_path});
            const openssl_lib_raw = std.fmt.allocPrint(b.allocator, "{s}\\lib", .{openssl_path});
            const openssl_lib = openssl_lib_raw catch "C:\\openssl\\include";
            defer b.allocator.free(openssl_lib);
            const openssl_include_raw = std.fmt.allocPrint(b.allocator, "{s}\\include", .{openssl_path});
            const openssl_include = openssl_include_raw catch "C:\\openssl\\include";
            defer b.allocator.free(openssl_include);

            exe.addLibraryPath(openssl_lib);
            exe.addIncludePath(openssl_include);

            exe.linkSystemLibrary("libssl");
        },
        else => {},
    }

    exe.linkSystemLibrary("c");
    exe.linkSystemLibrary("clamav");
    // This declares intent for the executable to be installed into the
    // standard location when the user invokes the "install" step (the default
    // step when running `zig build`).
    b.installArtifact(exe);

    // This *creates* a Run step in the build graph, to be executed when another
    // step is evaluated that depends on it. The next line below will establish
    // such a dependency.
    const run_cmd = b.addRunArtifact(exe);

    // By making the run step depend on the install step, it will be run from the
    // installation directory rather than directly from within the cache directory.
    // This is not necessary, however, if the application depends on other installed
    // files, this ensures they will be present and in the expected location.
    run_cmd.step.dependOn(b.getInstallStep());

    // This allows the user to pass arguments to the application in the build
    // command itself, like this: `zig build run -- arg1 arg2 etc`
    if (b.args) |args| {
        run_cmd.addArgs(args);
    }

    // This creates a build step. It will be visible in the `zig build --help` menu,
    // and can be selected like this: `zig build run`
    // This will evaluate the `run` step rather than the default, which is "install".
    const run_step = b.step("run", "Run the app");
    run_step.dependOn(&run_cmd.step);

    // Creates a step for unit testing. This only builds the test executable
    // but does not run it.
    const unit_tests = b.addTest(.{
        .root_source_file = .{ .path = "src/main.zig" },
        .target = target,
        .optimize = optimize,
    });

    const run_unit_tests = b.addRunArtifact(unit_tests);

    // Similar to creating the run step earlier, this exposes a `test` step to
    // the `zig build --help` menu, providing a way for the user to request
    // running the unit tests.
    const test_step = b.step("test", "Run unit tests");
    test_step.dependOn(&run_unit_tests.step);
}
