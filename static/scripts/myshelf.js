let updatebuttons = document.getElementsByClassName("update-shelf")
for(let i=0; i < updatebuttons.length; i++){
  updatebuttons[i].addEventListener('click', function(){
    let bookid = this.dataset.book
    let action = this.dataset.action
    console.log(bookid, action)
    if(user === 'AnonymousUser'){
      console.log('anon user')
    }else{
      updateuserorder(bookid, action);
    }
  })
}




function updateuserorder(bookid, action){
  console.log('user is logged in')
  var url = '/pages/update_item/'

  fetch(url, { 
    method:'POST',
    headers:{
      'Content-Type':'application/json',
      'X-CSRFToken':csrftoken
    },
    body:JSON.stringify({'bookid': bookid, 'action': action})
  })

  .then((response) =>{
    return response.json()
  })
  .then((data) =>{
    console.log(data)
  })
}







let updatethebuttons = document.getElementsByClassName("remove-shelf")
for(let i=0; i < updatethebuttons.length; i++){
  updatethebuttons[i].addEventListener('click', function(){
    let bookid = this.dataset.book
    let action = this.dataset.action
    console.log(bookid, action)
    if(user === 'AnonymousUser'){
      console.log('anon user')
    }else{
      updateuserorderneg(bookid, action);
    }
  })
}




function updateuserorderneg(bookid, action){
  console.log('user is logged in')
  var url = '/pages/delete_item/'

  fetch(url, { 
    method:'POST',
    headers:{
      'Content-Type':'application/json',
      'X-CSRFToken':csrftoken
    },
    body:JSON.stringify({'bookid': bookid, 'action': action})
  })

  .then((response) =>{  
    return response.json()
  })
  .then((data) =>{
    console.log(data)
  })
}










let addtohistorybuttons = document.getElementsByClassName("history-confirm")
for(let i=0; i < addtohistorybuttons.length; i++){
  addtohistorybuttons[i].addEventListener('click', function(){
    let bookid = this.dataset.book
    let action = this.dataset.action
    let startingdateInput = document.getElementById('starting-date');
    let thestartingdate = startingdateInput.value; 

    console.log(bookid, action, thestartingdate)
    if(user === 'AnonymousUser'){
      console.log('anon user')
    }else{
      additemtohistory(bookid, action, thestartingdate);
    }
  })
}




function additemtohistory(bookid, action, thestartingdate){
  console.log('user is logged in')
  var url = '/pages/update_history/'

  fetch(url, { 
    method:'POST',
    headers:{
      'Content-Type':'application/json',
      'X-CSRFToken':csrftoken
    },
    body:JSON.stringify({'bookid': bookid, 'action': action, 'thestartingdate': thestartingdate})
  })

  .then((response) =>{
    return response.json()
  })
  .then((data) =>{
    console.log(data)
  })
}










let returnbook = document.getElementsByClassName("return-book")
for(let i=0; i < returnbook.length; i++){
  returnbook[i].addEventListener('click', function(){
    let bookid = this.dataset.book
    let action = this.dataset.action
    let returningdateInput = document.getElementById('returning-date');
    let thereturningdate = returningdateInput.value; 
    console.log(bookid, action)
    if(user === 'AnonymousUser'){
      console.log('anon user')
    }else{
      returnthebook(bookid, action, thereturningdate);
    }
  })
}




function returnthebook(bookid, action, thereturningdate){
  console.log('user is logged in')
  var url = '/pages/return_book/'

  fetch(url, { 
    method:'POST',
    headers:{
      'Content-Type':'application/json',
      'X-CSRFToken':csrftoken
    },
    body:JSON.stringify({'bookid': bookid, 'action': action, 'thereturningdate': thereturningdate})
  })

  .then((response) =>{
    return response.json()
  })
  .then((data) =>{
    console.log(data)
  })
}

