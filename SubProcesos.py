import subprocess
import os


def record_on_run(newFileName):
    return subprocess.run(
        f"ffmpeg -f x11grab -framerate 120 -video_size 3440x1440 -i :1.0 -f pulse -i default -c:v libx264 -crf 18 -b:v 14000k -c:a aac -b:a 256k -preset ultrafast -tune zerolatency '{newFileName}'",
        shell=True,
    )


def record_on_popen(newFileName):
    return subprocess.Popen(
        f"ffmpeg -f x11grab -framerate 144 -video_size 3440x1440 -i :1.0 -f pulse -i default -c:v libx264 -crf 18 -b:v 5000k -c:a aac -b:a 256k -preset ultrafast -tune zerolatency '{newFileName}'",
        shell=True,
    )


def exec_command(command):
    return subprocess.Popen(command, shell=True)


def get_monitor_id(monitorDisplayPort):
    # return os.system("xrandr --listactivemonitors | grep -i " + monitorDisplayPort)
    result = subprocess.check_output(
    "xrandr --listactivemonitors | grep -i " + monitorDisplayPort,
    shell=True, text=True
    )
    return ":"+result.strip().split(":")[0]+".0"


# xrandr, para obtener información sobre el monitor.
# xrandr --listmonitors
# UBICACIÓN DÓNDE COLOCAR EL X,Y PARA GRABAR
# ffmpeg -f x11grab -framerate 60 -video_size 1280x720 -i :0.0+100,200 output.mp4
