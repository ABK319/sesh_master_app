import os 
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sesh_master_app.settings')


django.setup()
from django.core.files.base import ContentFile
from django.contrib.auth.models import User
from django.contrib.auth.models import  UserManager
from seshmaster.models import Nightclub


def populate():
	
	

	nightclubs = {"Name": ["Cathouse", "Firewater", "Sub Club", "The Garage", "Reflex"],
		"Music": ["Rock", "EDM", "Dance", "EDM", "80s"],
		"Price": ["£3", "£4.50", "$2.60", "$3", "£2.50"],
		"Desc": ["filler text one", "filler text two", "filler text three", "filler text four", "filler text five"],
		"Location": ["Argyle Street", "Cambell Lane", "Random Alley", "Forgotten Avenue", "Sauchiehall Street"],
		"Score": [3, 4, 5, 3, 4],
		"Image": []}
		
	users = {"User": ["seshlad420", "partygirl74", "SarahMathews12", "Carl Marks", "StevenAaron45"],
		"Email": ["random@email.com", "randomer@hotmail.net", "anonymous@gmail.com", "madeupname@outlook.com", "fifthrandomemail@email.co.uk"],
		"Password": ["password123", "passcode234", "mypassword1", "throwaway666", "outofideas"],
		"Image": [],}
		
		#"one.jpg", "two.jpg", "three.jpg", "four.jpg", "five.jpg"
		#"user1.jpg", "user2.jpg", "user3.jpg", "user4.jpg", "user5.jpg"
	
	directory1 = r'\WAD2 Project\sesh_master_app\Club_Images'
	for i in "one.jpg", "two.jpg", "three.jpg", "four.jpg", "five.jpg":
		filepath = directory1 + "\\" + i
		myf = open(filepath, 'rb')
		f = ContentFile(myf.read())
		f.name = filepath.split("/")[-1]
		f.size = os.path.getsize(filepath)
		nightclubs["Image"].append(f)
		
	directory2 = r'\WAD2 Project\sesh_master_app\\User_Images'
	for j in "user1.jpg", "user2.jpg", "user3.jpg", "user4.jpg", "user5.jpg":
		filepath = directory2 + "\\" + j
		myf = open(filepath, 'rb')
		f = ContentFile(myf.read())
		f.name = filepath.split("/")[-1]
		f.size = os.path.getsize(filepath)
		users["Image"].append(f)
		

	for i in range(5):
		Name = nightclubs["Name"][i]
		Music = nightclubs["Music"][i]
		Price = nightclubs["Price"][i]
		Desc = nightclubs["Desc"][i]
		Location = nightclubs["Location"][i]
		Score = nightclubs["Score"][i]
		Image = nightclubs["Image"][i]
		add_club(Name, Music, Price, Desc, Location, Score, Image)
		
			
	for j in range(5):
		User = users["User"][j]
		Email = users["Email"][j]
		Password = users["Password"][j]
		Image = users["Image"][j]
		add_user(User, Email, Password, Image)

	print("Database Successfully Populated.")
		
def add_club(Name, Music, Price, Desc, Location, Score, Image):
	c = Nightclub.objects.get_or_create(name=Name)[0]
	c.music_genre=Music
	c.price=Price
	c.description=Desc
	c.location=Location
	c.average_score=Score
	c.img=Image
	c.save()
	
	return c
	
	
def add_user(Username, Email, Pass, Image):
	u = User.objects.create_user(username=Username, email=Email, password=Pass)
	
	return(u)
	#User.objects.get_or_create(username=Username)[0]
	#u.email=Email
	#u.set_password=Pass
	#u.picture=Image
if __name__ == '__main__':
	print("Starting population script...")
	print("...")
	try:
		populate()
	except:
		print("=============Warning!=============")
		print("Script was previously run.")
		print("User and Nightclub data already ")
		print("present in database.")
		print("Cancelling script...")
		print("=================================")
		