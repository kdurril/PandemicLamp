
# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)

def do_connect():
    import network
    SSID = '{}'
    PASSWORD = '{}'
    sta_if = network.WLAN(network.STA_IF)
    ap_if = network.WLAN(network.AP_IF)
    if ap_if.active():
        ap_if.active(False)
    if not sta_if.isconnected():
        print('connecting to network...')
        #sta_if.config(dhcp_hostname="circadian-lamp")
        sta_if.active(True)
        sta_if.connect(SSID, PASSWORD)
        while not sta_if.isconnected():
            pass
    print('Network configuration:', sta_if.ifconfig())
    import ntptime
    ntptime.host = '3.north-america.pool.ntp.org'
    ntptime.settime()
do_connect()

#import webrepl
#webrepl.start()
