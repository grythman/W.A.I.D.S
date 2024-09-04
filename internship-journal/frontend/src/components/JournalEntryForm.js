import React, { useState } from "react";
import { createJournalEntry } from "../services/api";

const JournalEntryForm = ({ setJournalEntries }) => {
  const [content, setContent] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    const newJournalEntry = {
      content,
      date: new Date().toISOString().split("T")[0],
    };
    const response = await createJournalEntry(newJournalEntry);
    setJournalEntries((prev) => [...prev, response.data]);
    setContent("");
  };

  return (
    <form onSubmit={handleSubmit}>
      <textarea
        placeholder="Journal Content"
        value={content}
        onChange={(e) => setContent(e.target.value)}
      />
      <button type="submit">Add Journal Entry</button>
    </form>
  );
};

export default JournalEntryForm;
