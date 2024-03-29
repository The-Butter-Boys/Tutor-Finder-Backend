## This is more of a brainstorming area for before we started on the codebase--Not proper, up-to-date API documentation.


## Model Schemas
**i.e. what the database tables store**
### USERS
```
{
  id: <int>,
  username: <string>,
  password_hash: <string>,
  email: <string>,
}
```

### COURSES
```
{
  id: <int>,
  department: <string>,
  number: <string>,
  name: <string>
}
```

### USER COURSES
```
{
  id: <int>,
  user_id: <int>,
  course_id: <int>,
  type: <enum: 'student' or 'tutor'>
}
```
## Objects Returned From API Routes

### \<User\>
```
{
  id: <int>,
  username: <string>,
  email: <string>,
  tutor_courses: [<Course>, ..., <Course>],
  student_courses: [<Course>, ..., <Course>]
}
```


### \<Course\>
```
{
  id: <int>,
  department: <string>,
  number: <string>
  name: <string>,
}
```

## API Routes

### GET routes


<hr>

### `/users`

Returns all users

RETURNS: `[<User>, ..., <User>]`


<hr>

### `/users/<id>`

Returns user by id

RETURNS: `<User>`


<hr>

### `/users/<id>/courses/student`

Returns all student courses of user by id

RETURNS: `[<Course>, ..., <Course>]`


<hr>

### `/users/<id>/courses/tutor`

Returns all tutor courses of user by id

RETURNS: `[<Course>, ..., <Course>]`


<hr>

### `/tutors`

Returns all tutors

RETURNS: `[<User>, ..., <User>]`


<hr>

### `/students`

Returns all students

RETURNS: `[<User>, ..., <User>]`

<hr>

### `/courses`

Returns all courses available in the catalog

RETURNS: `[<Course>, ..., <Course>]`

<hr>

### `/courses/<id>`

Returns course by id

RETURNS: `<Course>`


<hr>

### POST routes


<hr>

### `/users`

EXPECTS: 

```
{
  username: <string>,
  password: <string>,
  email: <string>
}
```

<hr>

### `/courses`

EXPECTS:

```
{
  department: <string>,
  number: <string>,
  name: <string>
}
```
<hr>