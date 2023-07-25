package com.example.rater;

import android.content.Intent;
import android.os.Bundle;
import android.widget.Button;
import android.widget.EditText;
import androidx.appcompat.app.AppCompatActivity;
import java.util.Collections;
import java.util.List;

public class MovieInputActivity extends AppCompatActivity {

    EditText titleEdTxt, genreEdTxt, runtimeEdTxt, castEdTxt, directorEdTxt, descEdTxt;
    Button inputButton;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_movie_input);

        titleEdTxt = findViewById(R.id.input_title);
        genreEdTxt = findViewById(R.id.input_genre);
        runtimeEdTxt = findViewById(R.id.input_runtime);
        castEdTxt = findViewById(R.id.input_cast);
        directorEdTxt = findViewById(R.id.input_director);
        descEdTxt = findViewById(R.id.input_description);

        inputButton = findViewById(R.id.input_button);

        inputButton.setOnClickListener(view -> {
            String title = titleEdTxt.getText().toString();
            String genre = genreEdTxt.getText().toString();
            String runtime = runtimeEdTxt.getText().toString();
            List<String> cast = Collections.singletonList(castEdTxt.getText().toString());
            String director = directorEdTxt.getText().toString();
            String description = descEdTxt.getText().toString();

            MovieInput input = new MovieInput(title, genre, runtime, cast, director, description);

            Intent intent = new Intent(MovieInputActivity.this, PredictActivity.class);
            intent.putExtra("input", input);
            MovieInputActivity.this.startActivity(intent);
        });
    }
}
