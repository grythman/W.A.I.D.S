// EvaluationPage.js
import React from 'react';

const EvaluationPage = () => {
    return (
        <div className="evaluation-page">
            <h2>Evaluate Student</h2>
            <form>
                <label>Performance Rating:</label>
                <input type="number" min="1" max="10" />

                <label>Feedback:</label>
                <textarea rows="5"></textarea>

                <button type="submit">Submit Evaluation</button>
            </form>
        </div>
    );
}

export default EvaluationPage;
