# Contact Book

We come across lots of people daily. We make acquaintances and friends. We get their contacts to keep in touch later on. Sadly, keeping the received contact details can be hard. One way to do this is to write the contact details down. But this is not secure as the physical book can easily be lost.

This is where the Contact Book project comes in. A contact book is a tool for saving a contact’s details, such as name, address, phone number, and email address. With this contact book project, you can build a software tool that people can use to save and find contact details.

With the contact book project idea, users can save their contacts with less risk of losing the saved contact details. It’ll always be accessible from their computer, through the command-line.

## Technical Details

The main objective of this project is to save contact details. It’s important that you set up the commands users can use to enter the contact details. You can use the argparse or click command-line frameworks. They abstract a lot of complex stuff, so you only have to focus on the logic to be run when executing commands.

Some features you should implement includethe commands to

* delete contacts
* update contact information,
* and list saved contacts.
* You can also allow users to list contacts using different parameters, such as alphabetical order or contact creation date.

Since it’s a command-line project, the SQLite database will be fine for saving contacts. SQLite is user-friendly to set up. You may save the contact details in a file, but a file will not offer the benefits you can gain from using SQLite, such as performance and security.

* To use the SQLite database in this project, the Python sqlite3 module will be very useful.

## Extra Challenge

Remember how the database is stored on the user’s computer? What if something happens, like the user losing their files? It means they’ll also lose the contact details.

You can challenge yourself further and backup the database to an online storage platform. To do this, you can upload the database files to the cloud at certain intervals.

You can also add a command that allows users to backup the database themselves. This way, the user can still have access to the contacts if the database file is lost.

You should note that you may need some form of identification, so the contact book can tell which database file belongs to which user. Implementing a user authentication feature is one way to go about it.

## Contact

Uses a class to make a contact tile which will be converted to json to be saved

* Contact
  * Update

``` py

   udit = Contact('Udit')
   print(udit.__dict__)
   udit.Update(('Email', 'uditknishad2119@gmail.com'))
   udit.Update(('PhoneNumbers', [9503802165, 8484023074, 9975177395]))
   udit.Update(('Name', 'Udit Kumar Nishad'))
   print(udit.__dict__)

```

## DatabaseHandler

Handles the contact updating and database syncing using json.

* Handler
  * AddContact
  * GetDatabase
  * Sync

``` py

    udit = Contact('Udit', 3011958)
    bhum = Contact('Bhum', 4565445654)

    db = Handler()

    db.AddContact(udit)
    db.AddContact(bhum)

    udit.Update("PhoneNumbers", 8484023074)
    udit.Update('Email', 'uditknishad2119@gmail.com')

    ary = Contact('Aryan', 7789453211)
    db.AddContact(ary)

    ary.Update('Email', 'aryanjagtap@gmail.com')

    db.Sync()

```
