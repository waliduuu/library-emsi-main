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