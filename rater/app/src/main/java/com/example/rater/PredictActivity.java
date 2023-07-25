package com.example.rater;

import android.content.Intent;
import android.os.Bundle;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

import com.chaquo.python.PyObject;
import com.chaquo.python.Python;
import com.chaquo.python.android.AndroidPlatform;

public class PredictActivity extends AppCompatActivity {

    TextView textView;

    MovieInput mInput;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_predict);

        textView = findViewById(R.id.textview);

        Intent intent = getIntent();
        mInput = (MovieInput) intent.getSerializableExtra("input");

        if (! Python.isStarted()) {
            Python.start(new AndroidPlatform(this));
        }

        Python py = Python.getInstance();

        PyObject pyObject = py.getModule("test");

        PyObject pyObj = pyObject.callAttr("predict", mInput.getTitle(), mInput.getGenre(), mInput.getRuntime(),
                                            mInput.getCast(), mInput.getDirector(), mInput.getDescription());

        textView.setText(pyObj.toString());
    }
}
