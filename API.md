
"User object" and "Course object" are used to simplify JSON examples below. They're provided here for reference.

`User object`:
```json
{
	"id": <int>,
	"username": <string>,
	"email": <string>
}
```

`Course object`:
```json
{
	"id": <int>,
	"department": <string>,
	"number": <string>,
	"name": <string>
}
```
---

## `POST /register`

Registers new user and returns auth token

### **Payload**
```json
{
	"username": <string>,
	"email": <string>,
	"password": <string>
}
```

### **Response**


`200:`
```json
{
	"token": <token>,
	"user": <User object>
}
```


---

## `POST /login`

Logs in user and returns auth token

### **Payload**
```json
{
	"username": <string>,
	"password": <string>
}
```

### **Response**

`200:`
```json
{
	"token": <token>,
	"user": <User object>
}
```

---

## `GET /user`

**Auth token required**

Gets the user associated with token

### **Payload**

None


### **Response**

`200:`
```json
{
	"user": <User object>
}
```

---

## `GET /user/courses`

**Auth token required**

Gets the courses of the user associated with the token

### **Payload**

None


### **Response**
`200:`
```json
{
	"user": <User object>,
	"courses": <list of Course objects>
}
```

---

## `POST /user/courses`

**Auth token required**

Add course to user associated with the token

### **Payload**

```json
{
	"course_id": <int>
}
```

### **Response**

`200:`
```json
{
	"user": <User object>,
	"courses": <list of Course objects>
}
```

---

## `GET /courses`

Get all the courses in the database

### **Payload**

None

### **Response**

`200:`
```json
{
	"courses": <list of Course objects>
}
```

---

## `POST /courses`

**Auth token required**

Add a course to all courses

### **Payload**
```json
{
	"department": <string>,
	"number": <string>,
	"name": <string>
}
```

### **Response**

`200:`
```json
{
	"id": <int>
	"department": <string>,
	"number": <string>,
	"name": <string>
}
```


---