AIR = """
<style>
@media print {
  *,
  *:before,
  *:after {
    background: transparent !important;
    color: #000 !important;
    box-shadow: none !important;
    text-shadow: none !important;
  }

  a,
  a:visited {
    text-decoration: underline;
  }

  a[href]:after {
    content: " (" attr(href) ")";
  }

  abbr[title]:after {
    content: " (" attr(title) ")";
  }

  a[href^="#"]:after,
  a[href^="javascript:"]:after {
    content: "";
  }

  pre,
  blockquote {
    border: 1px solid #999;
    page-break-inside: avoid;
  }

  thead {
    display: table-header-group;
  }

  tr,
  img {
    page-break-inside: avoid;
  }

  img {
    max-width: 100% !important;
  }

  p,
  h2,
  h3 {
    orphans: 3;
    widows: 3;
  }

  h2,
  h3 {
    page-break-after: avoid;
  }
}

html {
  font-size: 12px;
}

@media screen and (min-width: 32rem) and (max-width: 48rem) {
  html {
    font-size: 15px;
  }
}

@media screen and (min-width: 48rem) {
  html {
    font-size: 16px;
  }
}

body {
  line-height: 1.85;
}

p,
.air-p {
  font-size: 1rem;
  margin-bottom: 1.3rem;
}

h1,
.air-h1,
h2,
.air-h2,
h3,
.air-h3,
h4,
.air-h4 {
  margin: 1.414rem 0 .5rem;
  font-weight: inherit;
  line-height: 1.42;
}

h1,
.air-h1 {
  margin-top: 0;
  font-size: 3.998rem;
}

h2,
.air-h2 {
  font-size: 2.827rem;
}

h3,
.air-h3 {
  font-size: 1.999rem;
}

h4,
.air-h4 {
  font-size: 1.414rem;
}

h5,
.air-h5 {
  font-size: 1.121rem;
}

h6,
.air-h6 {
  font-size: .88rem;
}

small,
.air-small {
  font-size: .707em;
}

/* https://github.com/mrmrs/fluidity */

img,
canvas,
iframe,
video,
svg,
select,
textarea {
  max-width: 100%;
}

@import url(http://fonts.googleapis.com/css?family=Open+Sans:300italic,300);

body {
  color: #444;
  font-family: 'Open Sans', Helvetica, sans-serif;
  font-weight: 300;
  margin: 6rem auto 1rem;
  max-width: 48rem;
  text-align: center;
}

img {
  border-radius: 50%;
  height: 200px;
  margin: 0 auto;
  width: 200px;
}

a,
a:visited {
  color: #3498db;
}

a:hover,
a:focus,
a:active {
  color: #2980b9;
}

pre {
  background-color: #fafafa;
  padding: 1rem;
  text-align: left;
}

blockquote {
  margin: 0;
  border-left: 5px solid #7a7a7a;
  font-style: italic;
  padding: 1.33em;
  text-align: left;
}

ul,
ol,
li {
  text-align: left;
}

p {
  color: #777;
}

@import "furtive-print";
@import "furtive-typescale";
@import "furtive-responsive-utils";

@import url(http://fonts.googleapis.com/css?family=Open+Sans:300italic,300);

body {
  color: #444;
  font-family: 'Open Sans', Helvetica, sans-serif;
  font-weight: 300;
  margin: 6rem auto 1rem;
  max-width: 48rem;
  text-align: center;
}

img {
  border-radius: 50%;
  height: 200px;
  margin: 0 auto;
  width: 200px;
}

a,
a:visited {
  color: #3498db;
}

a:hover,
a:focus,
a:active {
  color: #2980b9;
}

pre {
  background-color: #fafafa;
  padding: 1rem;
  text-align: left;
}

blockquote {
  margin: 0;
  border-left: 5px solid #7a7a7a;
  font-style: italic;
  padding: 1.33em;
  text-align: left;
}

ul,
ol,
li {
  text-align: left;
}

p {
  color: #777;
}
</style>
"""

SPLENDOR = """<style>@media print{*,:after,:before{background:0 0!important;color:#000!important;box-shadow:none!important;text-shadow:none!important}a,a:visited{text-decoration:underline}a[href]:after{content:" (" attr(href) ")"}abbr[title]:after{content:" (" attr(title) ")"}a[href^="#"]:after,a[href^="javascript:"]:after{content:""}blockquote,pre{border:1px solid #999;page-break-inside:avoid}thead{display:table-header-group}img,tr{page-break-inside:avoid}img{max-width:100%!important}h2,h3,p{orphans:3;widows:3}h2,h3{page-break-after:avoid}}@media screen and (min-width:32rem) and (max-width:48rem){html{font-size:15px}}@media screen and (min-width:48rem){html{font-size:16px}}body{line-height:1.85}.splendor-p,p{font-size:1rem;margin-bottom:1.3rem}.splendor-h1,.splendor-h2,.splendor-h3,.splendor-h4,h1,h2,h3,h4{margin:1.414rem 0 .5rem;font-weight:inherit;line-height:1.42}.splendor-h1,h1{margin-top:0;font-size:3.998rem}.splendor-h2,h2{font-size:2.827rem}.splendor-h3,h3{font-size:1.999rem}.splendor-h4,h4{font-size:1.414rem}.splendor-h5,h5{font-size:1.121rem}.splendor-h6,h6{font-size:.88rem}.splendor-small,small{font-size:.707em}canvas,iframe,img,select,svg,textarea,video{max-width:100%}@import url(http://fonts.googleapis.com/css?family=Merriweather:300italic,300);html{font-size:18px;max-width:100%}body{color:#444;font-family:Merriweather,Georgia,serif;margin:0;max-width:100%}:not(div):not(img):not(body):not(html):not(li):not(blockquote):not(p),p{margin:1rem auto;max-width:36rem;padding:.25rem}div,div img{width:100%}blockquote p{font-size:1.5rem;font-style:italic;margin:1rem auto;max-width:48rem}li{margin-left:2rem}h1{padding:4rem 0!important}p{color:#555;height:auto;line-height:1.45}code,pre{font-family:Menlo,Monaco,"Courier New",monospace}pre{background-color:#fafafa;font-size:.8rem;overflow-x:scroll;padding:1.125em}a,a:visited{color:#3498db}a:active,a:focus,a:hover{color:#2980b9}</style>"""


RETRO = """<style>
pre,
code {
  font-family: Menlo, Monaco, "Courier New", monospace;
}

pre {
  padding: .5rem;
  line-height: 1.25;
  overflow-x: scroll;
}

@media print {
  *,
  *:before,
  *:after {
    background: transparent !important;
    color: #000 !important;
    box-shadow: none !important;
    text-shadow: none !important;
  }

  a,
  a:visited {
    text-decoration: underline;
  }

  a[href]:after {
    content: " (" attr(href) ")";
  }

  abbr[title]:after {
    content: " (" attr(title) ")";
  }

  a[href^="#"]:after,
  a[href^="javascript:"]:after {
    content: "";
  }

  pre,
  blockquote {
    border: 1px solid #999;
    page-break-inside: avoid;
  }

  thead {
    display: table-header-group;
  }

  tr,
  img {
    page-break-inside: avoid;
  }

  img {
    max-width: 100% !important;
  }

  p,
  h2,
  h3 {
    orphans: 3;
    widows: 3;
  }

  h2,
  h3 {
    page-break-after: avoid;
  }
}

a,
a:visited {
  color: #01ff70;
}

a:hover,
a:focus,
a:active {
  color: #2ecc40;
}

.retro-no-decoration {
  text-decoration: none;
}

html {
  font-size: 12px;
}

@media screen and (min-width: 32rem) and (max-width: 48rem) {
  html {
    font-size: 15px;
  }
}

@media screen and (min-width: 48rem) {
  html {
    font-size: 16px;
  }
}

body {
  line-height: 1.85;
}

p,
.retro-p {
  font-size: 1rem;
  margin-bottom: 1.3rem;
}

h1,
.retro-h1,
h2,
.retro-h2,
h3,
.retro-h3,
h4,
.retro-h4 {
  margin: 1.414rem 0 .5rem;
  font-weight: inherit;
  line-height: 1.42;
}

h1,
.retro-h1 {
  margin-top: 0;
  font-size: 3.998rem;
}

h2,
.retro-h2 {
  font-size: 2.827rem;
}

h3,
.retro-h3 {
  font-size: 1.999rem;
}

h4,
.retro-h4 {
  font-size: 1.414rem;
}

h5,
.retro-h5 {
  font-size: 1.121rem;
}

h6,
.retro-h6 {
  font-size: .88rem;
}

small,
.retro-small {
  font-size: .707em;
}

/* https://github.com/mrmrs/fluidity */

img,
canvas,
iframe,
video,
svg,
select,
textarea {
  max-width: 100%;
}

html,
body {
  background-color: #222;
  min-height: 100%;
}

html {
  font-size: 18px;
}

body {
  color: #fafafa;
  font-family: "Courier New";
  line-height: 1.45;
  margin: 6rem auto 1rem;
  max-width: 48rem;
  padding: .25rem;
}

pre {
  background-color: #333;
}

blockquote {
  border-left: 3px solid #01ff70;
  padding-left: 1rem;
}
</style>"""

MODEST = """<style>@media print {
  *,
  *:before,
  *:after {
    background: transparent !important;
    color: #000 !important;
    box-shadow: none !important;
    text-shadow: none !important;
  }

  a,
  a:visited {
    text-decoration: underline;
  }

  a[href]:after {
    content: " (" attr(href) ")";
  }

  abbr[title]:after {
    content: " (" attr(title) ")";
  }

  a[href^="#"]:after,
  a[href^="javascript:"]:after {
    content: "";
  }

  pre,
  blockquote {
    border: 1px solid #999;
    page-break-inside: avoid;
  }

  thead {
    display: table-header-group;
  }

  tr,
  img {
    page-break-inside: avoid;
  }

  img {
    max-width: 100% !important;
  }

  p,
  h2,
  h3 {
    orphans: 3;
    widows: 3;
  }

  h2,
  h3 {
    page-break-after: avoid;
  }
}

pre,
code {
  font-family: Menlo, Monaco, "Courier New", monospace;
}

pre {
  padding: .5rem;
  line-height: 1.25;
  overflow-x: scroll;
}

a,
a:visited {
  color: #3498db;
}

a:hover,
a:focus,
a:active {
  color: #2980b9;
}

.modest-no-decoration {
  text-decoration: none;
}

html {
  font-size: 12px;
}

@media screen and (min-width: 32rem) and (max-width: 48rem) {
  html {
    font-size: 15px;
  }
}

@media screen and (min-width: 48rem) {
  html {
    font-size: 16px;
  }
}

body {
  line-height: 1.85;
}

p,
.modest-p {
  font-size: 1rem;
  margin-bottom: 1.3rem;
}

h1,
.modest-h1,
h2,
.modest-h2,
h3,
.modest-h3,
h4,
.modest-h4 {
  margin: 1.414rem 0 .5rem;
  font-weight: inherit;
  line-height: 1.42;
}

h1,
.modest-h1 {
  margin-top: 0;
  font-size: 3.998rem;
}

h2,
.modest-h2 {
  font-size: 2.827rem;
}

h3,
.modest-h3 {
  font-size: 1.999rem;
}

h4,
.modest-h4 {
  font-size: 1.414rem;
}

h5,
.modest-h5 {
  font-size: 1.121rem;
}

h6,
.modest-h6 {
  font-size: .88rem;
}

small,
.modest-small {
  font-size: .707em;
}

/* https://github.com/mrmrs/fluidity */

img,
canvas,
iframe,
video,
svg,
select,
textarea {
  max-width: 100%;
}

@import url(http://fonts.googleapis.com/css?family=Open+Sans+Condensed:300,300italic,700);

@import url(http://fonts.googleapis.com/css?family=Arimo:700,700italic);

html {
  font-size: 18px;
  max-width: 100%;
}

body {
  color: #444;
  font-family: 'Open Sans Condensed', sans-serif;
  font-weight: 300;
  margin: 0 auto;
  max-width: 48rem;
  line-height: 1.45;
  padding: .25rem;
}

h1,
h2,
h3,
h4,
h5,
h6 {
  font-family: Arimo, Helvetica, sans-serif;
}

h1,
h2,
h3 {
  border-bottom: 2px solid #fafafa;
  margin-bottom: 1.15rem;
  padding-bottom: .5rem;
  text-align: center;
}

blockquote {
  border-left: 8px solid #fafafa;
  padding: 1rem;
}

pre,
code {
  background-color: #fafafa;
}</style>"""
