import requests
import os
category='Get_Offers_on_Popular_Cars'

car_image={
 "Jeep Compass":"https://imgd.aeplcdn.com/320x180/n/cw/ec/47051/compass-exterior-right-front-three-quarter-84.png?isig=0&q=80",
 "Toyata Glanza":"https://imgd.aeplcdn.com/320x180/n/cw/ec/112839/glanza-exterior-right-front-three-quarter-6.png?isig=0&q=80",
 "Tata Harrier EV":"https://imgd.aeplcdn.com/320x180/n/cw/ec/139585/harrier-ev-exterior-right-front-three-quarter-58.png?isig=0&q=80",
 "Skoda Slavia":"https://imgd.aeplcdn.com/320x180/n/cw/ec/175951/slavia-exterior-right-front-three-quarter-10.png?isig=0&q=80",
 "Volkswagen Virtus":"https://imgd.aeplcdn.com/320x180/n/cw/ec/144681/virtus-exterior-right-front-three-quarter-11.png?isig=0&q=80",
 "Honda Elevate":"https://imgd.aeplcdn.com/320x180/n/cw/ec/142515/elevate-exterior-right-front-three-quarter-29.png?isig=0&q=80",
 "Renault Kiger":"https://imgd.aeplcdn.com/320x180/n/cw/ec/208550/kiger-exterior-right-front-three-quarter-30.png?isig=0&q=80",
 "Renault Triber":"https://imgd.aeplcdn.com/320x180/n/cw/ec/199767/triber-exterior-right-front-three-quarter-26.png?isig=0&q=80"
}

os.makedirs(category,exist_ok=True)

headers={
 "User-Agent":"Mozilla/5.0"
}

for car_name,url in car_image.items():
    try:
      response=requests.get(url,headers=headers)
      if response.status_code == 200:
        filename=f'{category}/{car_name}.png'

        with open(filename,'wb') as f:
          f.write(response.content)

        print(f'Downloaded:{car_name}')
      else:
        print(f'Failed:{car_name}')
    except Exception as e:
      print(f'Error downloading {car_name}:{e}')


from email.message import EmailMessage
msg=EmailMessage()
msg['Subject']='sending png file through email'
msg['From']='thamizharasi6812@gmail.com'
msg['To']='lovelythamizh06@gmail.com'
msg.set_content('please find the png file attached to th email')

with open(f'Get_Offers_on_Popular_Cars/Jeep Compass.png','rb') as f:
  file_data=f.read()
  file_name=f.name

msg.add_attachment(file_data,
                   maintype='image',
                   subtype='png',
                   filename=file_name)

print('email')



