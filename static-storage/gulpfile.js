var gulp = require("gulp");
var minifyCSS = require("gulp-minify-css");
var uglify = require("gulp-uglify");

gulp.task('minify-css', function () {
    return gulp.src('/home/aimethierry/anni/blog/static-storage/css/*.css')
        .pipe(minifyCSS())
        .pipe(gulp.dest('/home/aimethierry/anni/blog/static-storage/build/css/'))
});

gulp.task('uglify', function () {
    return gulp.src('/home/aimethierry/anni/blog/static-storage/js/*.js')
        .pipe(uglify())
        .pipe(gulp.dest('/home/aimethierry/anni/blog/static-storage/build/js/'))
});

gulp.task('minify', ['minify-css', 'uglify'])
