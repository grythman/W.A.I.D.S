# scanner/zap_scan.py
from zapv2 import ZAPv2
import time

def start_scan(target_url):
    zap = ZAPv2()
    
    # Start the ZAP proxy
    zap.urlopen(target_url)
    time.sleep(2)
    
    # Start scanning
    scan_id = zap.ascan.scan(target_url)
    
    while int(zap.ascan.status(scan_id)) < 100:
        print(f"Scan progress: {zap.ascan.status(scan_id)}%")
        time.sleep(5)
    
    # Retrieve results
    results = zap.core.alerts(baseurl=target_url)
    return results
