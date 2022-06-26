
### \<User\>
```
{
  user_id: <int>,
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
  course_name: <string>,
  department: <string>,
  catalog_number: <string>
}
```

## API Routes
### `/users`

Returns all users

RETURNS: `[<User>, ..., <User>]`

### `/users/<id>`

Returns user by id

RETURNS: `<User>`

### `/users/<id>/courses`

Returns all courses of user by id

RETURNS: `[<Course>, ..., <Course>]`

### `/users/<id>/courses/student`

Returns all student courses of user by id

RETURNS: `[<Course>, ..., <Course>]`

### `/users/<id>/courses/tutor`

Returns all tutor courses of user by id

RETURNS: `[<Course>, ..., <Course>]`

### `/tutors`

Returns all tutors

RETURNS: `[<User>, ..., <User>]`

### `/students`

Returns all students

RETURNS: `[<User>, ..., <User>]`

### `/courses`

Returns all courses

RETURNS: `[<Course>, ..., <Course>]`

### `/courses/<id>`

Returns course by id

RETURNS: `<Course>`


## Model Schemas

### USERS
```
{
  id: <int>,
  username: <string>,
  email: <string>,
  rating: <double>
}
```

### COURSES
```
{
  id: <int>,
  department: <string>,
  course_number: <string>,
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