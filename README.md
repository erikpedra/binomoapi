# Sosial Media
Telegram : https://t.me/minsanztuy

# binomoapi
Binomo API  
Website    : https://autotradevip.com/en/  
Olmyptrade : https://youtu.be/zTZT7zDlmtU  
Binomo     : https://youtu.be/ww9rVMX5TK4  
IQ Option  : https://youtu.be/4i3YUEDRGWY  
Quotex     : https://www.youtube.com/channel/UCCqnm8XHUoc0Ude78RJwmoA  
Expert Option     : https://www.youtube.com/channel/UCCqnm8XHUoc0Ude78RJwmoA

### Import
```python
from binomoapi.stable_api import Binomo
```
### Login by ssid
if connect sucess return True,None  

if connect fail return False,None  
```python
from binomoapi.stable_api import Binomo
ssid = "3dcc23bf-e2fc-abfa-13c6-e4405972a4dd"
device_id = "b471722521af426a0fb61d3a1b71c41c"
account=Binomo(set_ssid=ssid,device_id=device_id)
check_connect,message=account.connect()
print(check_connect,message)
```
### Check_win & buy sample

```python
from binomoapi.stable_api import Binomo
ssid = "3dcc23bf-e2fc-abfa-13c6-e4405972a4dd"
device_id = "b471722521af426a0fb61d3a1b71c41c"
account=Binomo(set_ssid=ssid,device_id=device_id)
check_connect,message=account.connect()
asset="CRYIDX"
amount=1
dir="call"
check,data=account.buy(asset,amount,dir,1)
if check:
    uuid=data["uuid"]
    print(account.check_win(uuid)) 
```
### get_server_time

```python
from binomoapi.stable_api import Binomo
ssid = "3dcc23bf-e2fc-abfa-13c6-e4405972a4dd"
device_id = "b471722521af426a0fb61d3a1b71c41c"
account=Binomo(set_ssid=ssid,device_id=device_id)
check,message=account.connect()
if check:
    while True:
        print(account.get_server_time())
        time.sleep(1)
```
### Get Balance

```python
from binomoapi.stable_api import Binomo
ssid = "3dcc23bf-e2fc-abfa-13c6-e4405972a4dd"
device_id = "b471722521af426a0fb61d3a1b71c41c"
account=Binomo(set_ssid=ssid,device_id=device_id)
check,message=account.connect()
account.change_balance("PRACTICE")
balance=account.get_balance()
print(balance)
```
### Buy

```python
from binomoapi.stable_api import Binomo
ssid = "3dcc23bf-e2fc-abfa-13c6-e4405972a4dd"
device_id = "b471722521af426a0fb61d3a1b71c41c"
account=Binomo(set_ssid=ssid,device_id=device_id)
check,message=account.connect()
if check:
    account.change_balance("PRACTICE")
    asset="CRYIDX"
    amount=1
    dir="call"#"call"/"put"
    duration=1#minute
    print(account.buy(asset,amount,dir,duration))

```
### get candle

```python
from binomoapi.stable_api import Binomo
ssid = "3dcc23bf-e2fc-abfa-13c6-e4405972a4dd"
device_id = "b471722521af426a0fb61d3a1b71c41c"
account=Binomo(set_ssid=ssid,device_id=device_id)
check_connect,message=account.connect() not need login can work
asset="CRYIDX"
#you want candle start time at
utc_time_start_time=datetime.datetime(2021, 1, 1, 0, 0, 0, 0)
#you want candle end time at
utc_time_end_time=datetime.datetime(2021, 8, 10, 0, 0, 0, 0)
#time step
time_step=900#
while True:
    a=utc_time_start_time.strftime('%Y-%m-%dT%H:%M:00')
    candle=account.get_candle(asset,a,time_step)
    if len(candle["data"])==0:
        utc_time_start_time=utc_time_start_time-datetime.timedelta(days=1)
        continue
    k=[]
    print(candle)
    date_time_str=candle["data"][-1]["created_at"]
     
    date_time_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%dT%H:%M:%S.000000Z')
    date_time_shift_obj=date_time_obj-utc_time_start_time
    
    utc_time_start_time=utc_time_start_time+date_time_shift_obj
    if date_time_obj>=utc_time_end_time:
        break
```
### GET realtime candle

```python
from binomoapi.stable_api import Binomo
ssid = "3dcc23bf-e2fc-abfa-13c6-e4405972a4dd"
device_id = "b471722521af426a0fb61d3a1b71c41c"
account=Binomo(set_ssid=ssid,device_id=device_id)
check,message=account.connect()
account.change_balance("PRACTICE")
asset="CRYIDX"
while 1:
    print(account.start_candles_stream(asset))
```

### get_payment and check asset open

```python
from binomoapi.stable_api import Binomo
ssid = "3dcc23bf-e2fc-abfa-13c6-e4405972a4dd"
device_id = "b471722521af426a0fb61d3a1b71c41c"
account=Binomo(set_ssid=ssid,device_id=device_id)
check,message=account.connect()
account.change_balance("PRACTICE")
while 1:
    data_all = account.get_payment("free")#"free"/"standard"/"gold"/"vip"
    print(data_all)
```
