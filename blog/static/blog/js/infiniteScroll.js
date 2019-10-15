function InfiniteScroll(path, wrapperId, rastPage) {
    this.path = path;
    this.pNum = 2;
    this.wNode = document.getElementById(wrapperId);
    this.wrapperId = wrapperId;
    this.rastPage = rastPage;
    this.enable = true;
}
InfiniteScroll.prototype.detectScroll = function() {
    window.onscroll = function (ev) {
        if ((window.innerHeight + window.scrollY) >= document.body.offsetHeight) {
            this.getNewPost();
        }
    }.bind(this);
};
InfiniteScroll.prototype.getNewPost = function() {
    if (this.enable === false) return false;
    this.enable = false;
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() { // 요청에 대한 콜백.
        if (xhr.readyState == xhr.DONE) { // 요청이 완료.
            if (xhr.status == 200) { // 요청이 정상수행.
                this.pNum++;
                var childItems = this.getChildItemsByAjaxHTML(xhr.responseText);
            }
            if (this.rastPage > this.pNum) {
                this.enable = true;
            }
            return
        }
    }.bind(this);
    console.log(`${location.origin + this.path + this.pNum}`);
    xhr.open('GET', `${location.origin + this.path + this.pNum}`, true);
    xhr.send();
};

InfiniteScroll.prototype.getChildItemsByAjaxHTML = function(HTMLText) {
    var newHTML = document.createElement('html');
    newHTML.innerHTML = HTMLText;
    var childItems = newHTML.querySelectorAll(`#${this.wrapperId} > *`);
    this.appendNewItems(childItems);
};

InfiniteScroll.prototype.appendNewItems = function(items) {
    items.forEach(item => {
        this.wNode.appendChild(item);
    });
};
