package com.example.rater;

import java.io.Serializable;
import java.util.List;

public class MovieInput implements Serializable {

    private String title;
    private String genre;
    private String runtime;
    private List<String> cast;
    private String director;
    private String description;

    public MovieInput(String title, String genre, String runtime, List<String> cast, String director, String description) {
        this.title = title;
        this.genre = genre;
        this.runtime = runtime;
        this.cast = cast;
        this.director = director;
        this.description = description;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public String getGenre() {
        return genre;
    }

    public void setGenre(String genre) {
        this.genre = genre;
    }

    public String getRuntime() {
        return runtime;
    }

    public void setRuntime(String runtime) {
        this.runtime = runtime;
    }

    public List<String> getCast() {
        return cast;
    }

    public void setCast(List<String> cast) {
        this.cast = cast;
    }

    public String getDirector() {
        return director;
    }

    public void setDirector(String director) {
        this.director = director;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
}
