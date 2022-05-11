// Scroll Back To Top Button
mybutton = document.getElementById("myBtn");


window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    mybutton.style.display = "block";
  } else {
    mybutton.style.display = "none";
  }
}


function topFunction() {
  document.body.scrollTop = 0; 
  document.documentElement.scrollTop = 0;
}

// Display random quotes
  var quotes = [
    {
    "quote": "We read to know that we are not alone.",
    "author": "William Nicholson"
  },
  {
    "quote": "A reader lives a thousand lives before he dies . . . The man who never reads lives only one.",
    "author": "George R.R. Martin"
  },
  {
    "quote": "Books were my pass to personal freedom. I learned to read at age three, and there discovered was a whole world to conquer that went beyond our farm in Mississippi.",
    "author": "Oprah Winfrey"
  },
  {
    "quote": "Show me a family of readers, and I will show you the people who move the world.",
    "author": "Napoléon Bonaparte"
  },
  {
    "quote": "Reading is essential for those who seek to rise above the ordinary.",
    "author": "Jim Rohn"
  },
  {
    "quote": "Today a reader, tomorrow a leader.",
    "author": "Margaret Fuller"
  },
  {
    "quote": "I kept always two books in my pocket, one to read, one to write in.",
    "author": "Jim Rohn"
  },
  {
    "quote": "Reading is essential for those who seek to rise above the ordinary.",
    "author": "Robert Louis Stevenson"
  },
  {
    "quote": "Think before you speak. Read before you think.”",
    "author": "Fran Lebowitz"
  },
  {
    "quote": "The reading of all good books is like conversation with the finest (people) of the past centuries.",
    "author": "Descartes"
  }
];


function generateQuote() {
    var randomNumber = Math.floor(Math.random() * quotes.length);
    var quote = quotes[randomNumber];
//    document.getElementById("quote").textContent = quote.quote;
//    document.getElementById("author").textContent = quote.author;
    $("#quote, #author").fadeOut(750, function(){
        $("#quote").text(quote.quote);
        $("#author").text(quote.author);
        $(this).fadeIn(750);
    });
}

function tweetThis() {
    var url = "https://twitter.com/intent/tweet";
    var text = document.getElementById('quote').textContent;
    var author = document.getElementById('author').textContent;
    window.open(url+"?text=" + "\"" + text + "\"" + " " + author);
}

generateQuote();
