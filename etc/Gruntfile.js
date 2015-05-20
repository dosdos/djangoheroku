module.exports = function (grunt) {

    var path = require('path');

    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),
        jshint: {
            options: {
                curly: true,
                eqeqeq: true,
                eqnull: true,
                browser: true,
                globals: {
                    jQuery: true
                }
            },
            myFiles: [
                '../frontoffice/static/frontoffice/js/*.js'
            ]
        },
        uglify: {
            default: {
                files: [
                    {
                        expand: true,
                        cwd: '../frontoffice/static/frontoffice/js',
                        src: '*.js',
                        dest: '../frontoffice/static/frontoffice/js/min',
                        ext: '.min.js'
                    }
                ]
            }
        },
        less: {
            development: {
                options: {
                    compress: true,
                    yuicompress: true,
                    optimization: 2
                },
                files: {
                    "../frontoffice/static/frontoffice/css/style.css": "../frontoffice/static/frontoffice/less/style.less"
                }
            }
        },
        watch: {
            files: [
                "../frontoffice/static/frontoffice/less/*",
                "../frontoffice/static/frontoffice/js/*"
            ],
            tasks: ["less", "jshint", "uglify"]
        }
    });

    // Load the plugins that provide the uglify, less and watch tasks.
    grunt.loadNpmTasks('grunt-contrib-jshint');
    grunt.loadNpmTasks('grunt-contrib-uglify');
    grunt.loadNpmTasks('grunt-contrib-less');
    grunt.loadNpmTasks('grunt-preen');
    grunt.loadNpmTasks('grunt-contrib-watch');

    // Default task(s).
    grunt.registerTask('default', ['uglify', 'less', 'preen']);

};