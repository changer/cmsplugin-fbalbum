#Facebook Album plugin for Django CMS

There are lot of useful plugins for Django CMS, here is another one. Well, this plugin works in an interesting way. As the name suggests this plugins lets you use the images from a facebook album. As of now, it support images from a facebook page's album.


All you need to do is to put the Facebook Album URL, Accesstoken and the album name and boom , you have a nice thumbnal in the desired place and when you click it big images will slide in carousel effects. Sounds nice, take a look here.

- Entering the info

![Admin Page](img/admin.png)

- Thumbnail view of Plugin

![Small View] (img/smallview.png)

- Big Images in Carousel

![Carousel](img/bigview.png)


#Installation

Installation is dead simple. First start your virtualenv

    $ workon sample
    (sample)$ pip install cmsplugin-fbalbum

Bazzinga! It is installed.


There might be some other things you will have to do if you are getting some sort of database error.

    python manage.py syncdb
    python manage.py migrate

Incase you face any problems, file an issue and Pull Requests are welcome.


