let updatebuttons = document.getElementsByClassName("update-shelf")
for(let i=0; i < updatebuttons.length; i++){
  updatebuttons[i].addEventListener('click', function(){
    let bookISBN = this.dataset.bookisbn
    let action = this.dataset.action
    console.log(bookISBN, action)
    if(user === 'AnonymousUser'){
      console.log('anon user')
    }else{
      updateuserorder(bookISBN, action);
    }
  })
}


function updateuserorder(bookISBN, action){
  console.log('user is logged in')
  var url = '/pages/update_item/'

  fetch(url, { 
    method:'POST',
    headers:{
      'Content-Type':'application/json',
      'X-CSRFToken':csrftoken
    },
    body:JSON.stringify({'bookISBN': bookISBN, 'action': action})
  })

  .then((response) =>{
    return response.json()
  })
  .then((data) =>{
    console.log(data)
  })
}