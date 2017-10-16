# -*- coding: utf-8 -*-
import web
import motortest

urls = (
    "/right", "right",
    "/left", "left"
)
app = web.application(urls, globals())

class right:        
    def GET(self):
        dick = motortest.move(1,2)
        #if not name: 
        #    name = 'World'
        return 'Hello right' + str(dick)

class left:        
    def GET(self):
        dick = motortest.move(0,2)
        #if not name: 
        #    name = 'World'
        return 'Hello left' + str(dick)

app = web.application(urls, globals())
app.run()
