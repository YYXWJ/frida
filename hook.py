import frida
import sys
rdev = frida.get_remote_device()
session = rdev.attach("com.example.administrator.myapplication")
#pid = rdev.spawn(["com.tencent.tmgp.pubgmhd"])
#session = rdev.attach(pid)
#rdev.resume(pid)
scr = """

Java.perform(function () {
    var runtime = Java.use('android.app.ContextImpl');
	var Log = Java.use("android.util.Log");
        var Throwable = Java.use("java.lang.Throwable");
    runtime.registerReceiver.overload('android.content.BroadcastReceiver','android.content.IntentFilter','java.lang.String','android.os.Handler').implementation = function () {
    
        var args = arguments[0];
		send('args:'+args);
		
        console.log(Log.getStackTraceString(Throwable.$new()));
		var returnvar = this.registerReceiver(arguments[0],arguments[1],arguments[2],arguments[3]);
  
        return returnvar;
    }
});

"""
script = session.create_script(scr)
def on_message(message ,data):
    print message
script.on("message" , on_message)
script.load()
sys.stdin.read()
