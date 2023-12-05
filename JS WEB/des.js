function item(name,desc,review){
	this.name = name;
	this.desc = desc;
	this.review = review;
	this.setReview = function(){
		this.review =prompt(this.review) ;
		alert(this.review);
		}
}	
let Slavik = new item("Slavik","30yo","neural evil");
Slavik.setReview();