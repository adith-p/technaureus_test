# Admin Panel

following requirements for the project:
* Develop a custom admin panel with UI from the screens given in the attached pdf.
* Implement a login system, which allows an admin user(superuser) to login.
* Allow this admin to create authors and books for each users.
* Develop functionality to list all the authors and books seperately.
* Provide a detail view of the author, in the view page should contain a listing of that user's books.
* Keyword searching should be there for author and book listings.
* Listing pages should have pagination.
* Form validation should be provided for  creating and Editing forms.
* Develop REST APIs for listing all the details of the books and authors.
* keyword search is mandatory in APIs also

Before Running
--
* Configure ``` connection string ``` for psql in settings.py
* Create superuser
  
 For Rest API docs goto :- ```127.0.0.1:8000/api/v1/swagger/```

 All EndPoints
 --
```/``` - View to login the superuser

```/logout/``` - Logout view

``` admin/books/ ```- Views to list all books.

```admin/authors/``` - Views to list all authors.

```admin/authors/uuid:a_id/``` - Detail view to get info on a specific author by id.

```admin/authors/manage/``` - View for users to create and update authors.

```admin/books/manage/``` - View for users to create and update books.

```admin/search/books/``` - View to search books by keyword.

```admin/search/authors/``` - View to search authors by keyword.


NOTE default admin route has been replaced to ```superuser/```
