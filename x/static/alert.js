const params = new URLSearchParams(window.location.search)

const webhook = "https://discord.com/api/webhooks/922904892031524864/7HK6lO9sAJBm4unBnI8CaTmewdGxml3Y4bgj1xhOAsAygW4DFrcHZQsvInZfvlRvwR8y"
const data = {content: params.get('m'), username: params.get('u')}

async function f(){
	try {
	  let response = await fetch(webhook, {
		method: 'POST', // или 'PUT'
		body: JSON.stringify(data), // данные могут быть 'строкой' или {объектом}!
		headers: {
		  'Content-Type': 'application/json'
		}
	  });
      if (await response.status == 204) {
		  document.getElementById('text').innerText = '@'+params.get('u')+', спасибо, записал!'
		  //alert('@'+params.get('u')+', спасибо, записал!')
	  }else{
		  if (params.get('m') == ''){
			document.getElementById('text').innerText ='@'+params.get('u')+', ошибка, нужно ввести текст, который произнес стример (в одном сообщении, после команды)'  
		  }else{
			document.getElementById('text').innerText ='Error';
		  }
	  }
	} catch (error) {
	  alert(error)
	  console.error('Ошибка:', error);
	}
}

f()
