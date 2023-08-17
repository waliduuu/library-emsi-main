const books = [
  {
    title : 'The mind of a leader',
    author : 'kevin Anderson',
    ISBN : 'D1111',
    Category : 'Self development',
    availablity : false 
  },
  {
    title : 'mastery',
    author : 'Rober Greene',
    ISBN : 'D1121',
    Category : 'Self development',
    availablity : true 
  },
    {
    title : 'power of habit',
    author : 'charles duhig',
    ISBN : 'D1121',
    Category : 'Self development',
    availablity : true 
  },
      {
    title : 'the 5am club',
    author : 'Robin charma',
    ISBN : 'D1121',
    Category : 'Self development',
    availablity : true 
  },
  {
    title : 'the great alone',
    author : 'christin hana',
    ISBN : 'D1121',
    Category : 'therapy',
    availablity : false 
  }
]

let bookshtml = '';

books.forEach((book) => {

  bookshtml += 
  `<div class="booksstats">
  <img class="bookimg" src="../img/books/${book.title}.png" alt="">
  <h4 class="bookstat">${book.title}</h4>
  <p class="bookstat">by : ${book.author}</p>
  <p class="bookstat">${book.Category}</p>
  `;
  if(book.availablity){
    bookshtml +=   
    `<div class="book-borrow-button-container">
    <button class="book-borrow-button" data-book-name="${book.title}">Borrow</button>
  </div>
</div>
</div>`;
  }else {
    bookshtml += 
    `<div class="book-borrow-button-container">
    <button class="book-not-borrow-button">Not Available</button>
  </div>
</div>
</div>`;
  }
});

document.querySelector('.latestbooks').innerHTML = bookshtml;

let cart = []
let matchingbooks = '';
document.querySelectorAll('.book-borrow-button')

  .forEach((button) => {
    button.addEventListener('click', () => {
      const bookName = button.dataset.bookName;
      cart.forEach((item) => {
        if (bookName === item.bookName){
          matchingbooks = item;
      };
    });

    if (matchingbooks){
      alert('you already asked to borrow this book, Check your library to edit his choice');
    } else{
      cart.push({
        bookName : bookName,
      });
    }
      console.log(cart);
    });
  });


