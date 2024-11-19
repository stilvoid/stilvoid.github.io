// Populate the sidebar
//
// This is a script, and not included directly in the page, to control the total size of the book.
// The TOC contains an entry for each page, so if each page includes a copy of the TOC,
// the total size of the page becomes O(n**2).
class MDBookSidebarScrollbox extends HTMLElement {
    constructor() {
        super();
    }
    connectedCallback() {
        this.innerHTML = '<ol class="chapter"><li class="chapter-item expanded affix "><a href="index.html">About</a></li><li class="chapter-item expanded affix "><li class="spacer"></li><li class="chapter-item expanded "><a href="projects.html"><strong aria-hidden="true">1.</strong> Projects</a></li><li><ol class="section"><li class="chapter-item expanded "><a href="tools.html"><strong aria-hidden="true">1.1.</strong> Tools</a></li><li class="chapter-item expanded "><a href="games.html"><strong aria-hidden="true">1.2.</strong> Games</a></li><li class="chapter-item expanded "><a href="music.html"><strong aria-hidden="true">1.3.</strong> Music</a></li></ol></li><li class="chapter-item expanded "><li class="spacer"></li><li class="chapter-item expanded "><a href="diary.html"><strong aria-hidden="true">2.</strong> Blog</a></li><li><ol class="section"><li class="chapter-item expanded "><a href="diary/2024-08-28.html"><strong aria-hidden="true">2.1.</strong> TBC</a></li><li class="chapter-item expanded "><a href="diary/2024-07-23.html"><strong aria-hidden="true">2.2.</strong> Back to the Primitive</a></li><li class="chapter-item expanded "><a href="diary/2019-11-13.html"><strong aria-hidden="true">2.3.</strong> Maur - A minimal AUR helper</a></li><li class="chapter-item expanded "><a href="diary/2019-02-12.html"><strong aria-hidden="true">2.4.</strong> Using Git with AWS CodeCommit Across Multiple AWS Accounts</a></li><li class="chapter-item expanded "><a href="diary/2018-11-08.html"><strong aria-hidden="true">2.5.</strong> git-get</a></li><li class="chapter-item expanded "><a href="diary/2018-08-14.html"><strong aria-hidden="true">2.6.</strong> Heroes: Building some old code</a></li><li class="chapter-item expanded "><a href="diary/2018-06-03.html"><strong aria-hidden="true">2.7.</strong> Shue</a></li><li class="chapter-item expanded "><a href="diary/2017-07-10.html"><strong aria-hidden="true">2.8.</strong> An evening of linux on the desktop</a></li><li class="chapter-item expanded "><a href="diary/2017-06-15.html"><strong aria-hidden="true">2.9.</strong> The day of linux on the desktop</a></li><li class="chapter-item expanded "><a href="diary/2016-02-25.html"><strong aria-hidden="true">2.10.</strong> Digital Subscriber</a></li><li class="chapter-item expanded "><a href="diary/2015-12-14.html"><strong aria-hidden="true">2.11.</strong> Ford</a></li><li class="chapter-item expanded "><a href="diary/2015-11-30.html"><strong aria-hidden="true">2.12.</strong> Sorted</a></li><li class="chapter-item expanded "><a href="diary/2015-09-17.html"><strong aria-hidden="true">2.13.</strong> Twofer</a></li><li class="chapter-item expanded "><a href="diary/2015-06-22.html"><strong aria-hidden="true">2.14.</strong> Pretty please</a></li><li class="chapter-item expanded "><a href="diary/2015-05-15.html"><strong aria-hidden="true">2.15.</strong> Andy and Teddy are waving goodbye</a></li><li class="chapter-item expanded "><a href="diary/2015-05-14.html"><strong aria-hidden="true">2.16.</strong> Building a componentised application</a></li><li class="chapter-item expanded "><a href="diary/2015-04-29.html"><strong aria-hidden="true">2.17.</strong> Why-fi?</a></li><li class="chapter-item expanded "><a href="diary/2015-03-12.html"><strong aria-hidden="true">2.18.</strong> Cleaning out my closet</a></li><li class="chapter-item expanded "><a href="diary/2015-01-02.html"><strong aria-hidden="true">2.19.</strong> Keychain and GnuPG &gt;= 2.1</a></li><li class="chapter-item expanded "><a href="diary/2014-12-09.html"><strong aria-hidden="true">2.20.</strong> Testing a Django app with Docker</a></li><li class="chapter-item expanded "><a href="diary/2014-12-01.html"><strong aria-hidden="true">2.21.</strong> Just call me Anneka</a></li><li class="chapter-item expanded "><a href="diary/2014-06-17.html"><strong aria-hidden="true">2.22.</strong> tmux</a></li><li class="chapter-item expanded "><a href="diary/2014-04-15.html"><strong aria-hidden="true">2.23.</strong> Netcat</a></li><li class="chapter-item expanded "><a href="diary/2014-01-31.html"><strong aria-hidden="true">2.24.</strong> btw</a></li><li class="chapter-item expanded "><a href="diary/2013-05-10.html"><strong aria-hidden="true">2.25.</strong> Things we learned at the LUG meet</a></li><li class="chapter-item expanded "><a href="diary/2013-02-11.html"><strong aria-hidden="true">2.26.</strong> Git aux</a></li><li class="chapter-item expanded "><a href="diary/2012-08-30.html"><strong aria-hidden="true">2.27.</strong> Lost at C</a></li><li class="chapter-item expanded "><a href="diary/2012-07-07.html"><strong aria-hidden="true">2.28.</strong> Ire</a></li><li class="chapter-item expanded "><a href="diary/2011-10-27.html"><strong aria-hidden="true">2.29.</strong> Break In!</a></li><li class="chapter-item expanded "><a href="diary/2011-10-22.html"><strong aria-hidden="true">2.30.</strong> xmodmap Hints and Tips</a></li></ol></li></ol>';
        // Set the current, active page, and reveal it if it's hidden
        let current_page = document.location.href.toString();
        if (current_page.endsWith("/")) {
            current_page += "index.html";
        }
        var links = Array.prototype.slice.call(this.querySelectorAll("a"));
        var l = links.length;
        for (var i = 0; i < l; ++i) {
            var link = links[i];
            var href = link.getAttribute("href");
            if (href && !href.startsWith("#") && !/^(?:[a-z+]+:)?\/\//.test(href)) {
                link.href = path_to_root + href;
            }
            // The "index" page is supposed to alias the first chapter in the book.
            if (link.href === current_page || (i === 0 && path_to_root === "" && current_page.endsWith("/index.html"))) {
                link.classList.add("active");
                var parent = link.parentElement;
                if (parent && parent.classList.contains("chapter-item")) {
                    parent.classList.add("expanded");
                }
                while (parent) {
                    if (parent.tagName === "LI" && parent.previousElementSibling) {
                        if (parent.previousElementSibling.classList.contains("chapter-item")) {
                            parent.previousElementSibling.classList.add("expanded");
                        }
                    }
                    parent = parent.parentElement;
                }
            }
        }
        // Track and set sidebar scroll position
        this.addEventListener('click', function(e) {
            if (e.target.tagName === 'A') {
                sessionStorage.setItem('sidebar-scroll', this.scrollTop);
            }
        }, { passive: true });
        var sidebarScrollTop = sessionStorage.getItem('sidebar-scroll');
        sessionStorage.removeItem('sidebar-scroll');
        if (sidebarScrollTop) {
            // preserve sidebar scroll position when navigating via links within sidebar
            this.scrollTop = sidebarScrollTop;
        } else {
            // scroll sidebar to current active section when navigating via "next/previous chapter" buttons
            var activeSection = document.querySelector('#sidebar .active');
            if (activeSection) {
                activeSection.scrollIntoView({ block: 'center' });
            }
        }
        // Toggle buttons
        var sidebarAnchorToggles = document.querySelectorAll('#sidebar a.toggle');
        function toggleSection(ev) {
            ev.currentTarget.parentElement.classList.toggle('expanded');
        }
        Array.from(sidebarAnchorToggles).forEach(function (el) {
            el.addEventListener('click', toggleSection);
        });
    }
}
window.customElements.define("mdbook-sidebar-scrollbox", MDBookSidebarScrollbox);
