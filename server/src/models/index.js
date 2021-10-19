const fs = require('fs')
const path = require('path')
const { config } = require('process')
const Sequelize = require('sequelize')
const cofig = require('../config/config')
const db = {}
const sequelize = new Sequelize(
    config.db.database,
    config.db.user,
    config.db.password,
    config.db.options,
)
module.exports = db