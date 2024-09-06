// ReportSubmission.js
import React from 'react';

const ReportSubmission = () => {
    return (
        <div className="report-submission">
            <h2>Submit Internship Report</h2>
            <form>
                <label>Company:</label>
                <input type="text" />

                <label>Role:</label>
                <input type="text" />

                <label>Duration:</label>
                <input type="text" />

                <label>Upload Report:</label>
                <input type="file" accept=".pdf,.docx" required />

                <button type="submit">Submit</button>
            </form>
        </div>
    );
}

export default ReportSubmission;
