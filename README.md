# Books CRUD Application

## Introduction

This application uses Python 3 and Django 3.0.3. It contains a `Books` module for managing book entities. 
Your job is to finish an implementation of the CRUD functionality using CBV.

## Task details
Please implement four class-based views (CBV) and mixins for them, so all unit tests will start passing. Also use `Django's messages framework` to add success/error messages.


### 1. **Implement `BookDetailView`** for showing the book. 

Your implementation should load book details data for given `isbn` parameter. If book for passed `isbn` doesn't exist, user should be redirected to a `'/books/'` default route (`BookListView`: `books:index`).

### 2. **Implement `BookCreateView`**  for creating a book. 

Your implementation should populate the form fields with a book's details. After successful submission user should be redirected to the page for the created book (`BookDetailView`: `books:detail`). And do not forget to add a validator to check a `isbn`, it can be separated into its parts with hyphens, so `isbn` may only contain digits and hyphens.

### 3. **Implement `BookUpdateView`**  for editing the book. 

Your implementation should populate the form fields with a book's details for passed `isbn` parameter. If book for passed `isbn` doesn't exist, user should be redirected to a `'/books/'` default route (`BookListView`: `books:index`). After successful submission user should be redirected to the page for the edited book (`BookDetailView`: `books:detail`).

### 4. **Implement `BookDeleteView`**  for deleting the book. 

Your implementation should delete a book for given `isbn` parameter. If book for passed `isbn` doesn't exist, user should be redirected to a `'/books/'` default route (`BookListView`: `books:index`). After the book is deleted, the user should be redirected to a list of books (`BookListView`: `books:index`).


## Hints

You shouldn't modify the unit tests, just complete the CBVs and mixins to make the unit tests run as expected.

To execute all unit tests, use:
    
    pip install -q -e . && nosetests


## TODOs

- Add nose for being able to run the unit tests
- Check if unit tests run (with or without nose)
- Add 404, 403 or 500 error pages
