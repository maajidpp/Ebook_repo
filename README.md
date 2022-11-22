# Ebook_repo

# EBOOK_PROJECT

#project setup-Ebook <br />
1st: Create or install virtualenvironment <br />
2nd: activate virtual environment <br />
clone this repository by typing “https://github.com/maajidpp/Ebook_repo.git” <br />
3rd: install requirments <br />

	command – pip install -r requirment.txt <br />

4th(runserver) – python manage.py runserver <br />
now you are good to go no more changes needed everything is setup (postman) <br />


#API DOCS <br />
To get access token <br />
	/api/ token <br />
	method- post <br />
	params – nil <br />
	body -  username, password <br />

 	sample - <br />
		{ <br />
			“username” : majid <br /> 
			“password” : 123 <br />
		} <br />
after this a access token will be given use this and add it in header as given below to get authenticated into other view or else will get 401 error <br />


	sample - <br />
		{ <br />
			“Authorization”: “bearer token” <br />
		} <br />

To get all ebooks <br />
	/get-all-ebooks <br /> 
	method – get <br />
	params -nil <br />
	body -nil <br />



To create ebook <br />
	/create-ebook <br />
	method – post <br />
	params – nil <br />
	body -  Title,  Author, Genre, Review, Favorite(optional true or false) <br />

	sample -
			{ 
				"Title": "welcome", <br />
				"Author": "pranav", <br />
				"Genre": "Fantasy", <br />
				"Review": 2 <br />
			} 



To update ebook <br />
	/update-ebook <br />
	method – put <br />
	params – nil <br />
	body - id (update the book first add id of the book) 	Title(new Title or old Title),  Author(old Author or new Author), Genre(new Genre or old Genre), Review(new Review or old Review), Favorite(new or old) <br />
	
	sample -  <br />
			{
				"id": "5", <br />
				"Title": "ebook", <br />
				"Author": "majid", <br />
				"Genre": "Fantasy", <br />
				"Review": 2 <br />
			}


To delete ebook <br />
	/delete-ebook/<int:id> <br />
	method – delete <br />
	params: id(id of ebook) <br />
	body – nil <br /> 
	
To search e-book <br />
	can enter a key and will match with every field and returns the value <br />
	method – post <br />
	params – nil <br />
	body – details(key to search) <br />

	sample - <br />
		{ <br />
			details:”p” <br />
		} <br />
