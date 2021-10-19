module.exports = (app) => {
    app.get('/test', (req, res) => {
        res.send({
            message: 'test test'
        })
    })
    
    app.post('/register', (req, res) => {
        res.send({
            message: `${req.body.email} user was registered`
        })
    })
}