// Q10: Create a database and work with MongoDB Query Language (Book Database)

// a) Creating a Database and Collection
use bookdb
db.createCollection("books")

// b) Insert Documents

// Insert a single document
db.books.insertOne({
  title: "DSA",
  author: "Pavan",
  price: 500
})

// Insert multiple documents
db.books.insertMany([
  {title: "DBMS", author: "John", price: 400},
  {title: "OS", author: "Smith", price: 300}
])

// c) Find All Books & Find with Condition

// Find all books
db.books.find()

// Find books with condition (price > 350)
db.books.find({price: {$gt: 350}})

// d) Update One Book & Multiple Books

// Update one book
db.books.updateOne(
  {title: "DSA"},
  {$set: {price: 600}}
)

// Update multiple books
db.books.updateMany(
  {},
  {$set: {publisher: "ABC"}}
)

// e) Delete Documents (One & Multiple Books)

// Delete one book
db.books.deleteOne({title: "OS"})

// Delete multiple books
db.books.deleteMany({price: {$lt: 400}})