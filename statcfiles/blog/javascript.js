function handleReply(response_id) {
    const reply_form_container = document.querySelector(`#replyFormContainer${response_id}`);
    if (reply_form_container) {
        reply_form_container.style.display = 'block';
    }
};

function handleCancel(response_id) {
    const reply_form_container = document.querySelector(`#replyFormContainer${response_id}`);
    if (reply_form_container) {
        reply_form_container.style.display = 'none';
    }
};

const toCommentButton = document.getElementById("goToComment");
const toTopButton = document.getElementById("goUp");
const toBottomButton = document.getElementById('goDown');
        // When the user scrolls down more than 375 px ffrom the top of the document, show the button
        window.onscroll = function () {
            if (document.body.scrollTop > 375 || document.documentElement.scrollTop > 375 ) {
                toTopButton.style.display = 'block';
                toCommentButton.style.display = 'block';
                // toBottomButton.style.display = 'none';
            } else {
                toTopButton.style.display = 'none';
                toCommentButton.style.display = 'none';
                // toBottomButton.style.display = 'block';
            }
            
        }


        // INTERACTION OBSERVER API TO OBSERVE IF FOOTER IS WITHIN 375PX OF WIEWPORT AND SET DISPLAY TO NONE
        // FOR THE TOBOTTOMBUTTON ELSE ITS TRUE 

let options = {
    root: null,
    rootMargin: '375px',
    threshold: 0
    }
    

// the callback we setup for the observer will be executed now for the first time
// it waits until we assign a target to our observer (even if the target is currently not visible)
// for more info https://blog.webdevsimplified.com/2022-01/intersection-observer/
// https://developer.mozilla.org/en-US/docs/Web/API/Intersection_Observer_API

const observer = new IntersectionObserver(function (entries, self) {
    entries.forEach(entry => {
      // Each entry describes an intersection change for one observed
      // target element:
      //   entry.boundingClientRect
      //   entry.intersectionRatio
      //   entry.intersectionRect
      //   entry.isIntersecting
      //   entry.rootBounds
      //   entry.target
      //   entry.time
      if (entry.isIntersecting) {
        toBottomButton.style.display = 'none';
      } else {
        toBottomButton.style.display = 'block';
      }
    });
  },options);
  observer.observe(document.getElementById('footer'));
  
            // END OF INTERSECTIONOBSERVER  API  SECTION 

function topFunction() {
    document.body.scrollTop = 0; // For Safari
    document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
    }
function downFunction() {
    document.body.scrollTo(0,document.body.scrollHeight); // For Safari
    document.documentElement.scrollTo(0,document.body.scrollHeight); // For Chrome, Firefox, IE and Opera
    }
function reloadPage() {
    // browsers automatically remembers where you left of with js cookies and take you there
    window.location.reload(); 
}