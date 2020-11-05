let Key = localStorage.getItem('theme-Color')

if(Key == null){
	Setcolor('Defult')
}else{
	Setcolor(Key)
}



let themeDotsColor = document.getElementsByClassName('theme-Color')



for (var i=0; themeDotsColor.length > i; i++){
	themeDotsColor[i].addEventListener('click', function(){
		let mode = this.dataset.mode
		console.log('Option clicked:', mode)
		Setcolor(mode)
	})
}


function Setcolor(mode){
	if(mode == 'Defult'){
		document.getElementById('theme-Color').href = '/static/css/Body-Button/style.css'
	}
	if(mode == 'Orange'){
		document.getElementById('theme-Color').href = '/static/css/Body-Button/Orange.css'
	}
	if(mode == 'Green'){
		document.getElementById('theme-Color').href = '/static/css/Body-Button/Green.css'
	}
	if(mode == 'Blue'){
		document.getElementById('theme-Color').href = '/static/css/Body-Button/Blue.css'
	}
	if(mode == 'Pink'){
		document.getElementById('theme-Color').href = '/static/css/Body-Button/Pink.css'
	}
	if(mode == 'Purple'){
		document.getElementById('theme-Color').href = '/static/css/Body-Button/Purple.css'
	}
	if(mode == 'Yellow'){
		document.getElementById('theme-Color').href = '/static/css/Body-Button/Yellow.css'
	}

	localStorage.setItem('theme-Color', mode)
}
