import React, { useState, useEffect } from 'react';
import { fetchJournalEntries } from '../services/api';
import JournalEntryForm from './JournalEntryForm';

const JournalEntryList = () => {
  const [journalEntries, setJournalEntries] = useState([]);

  useEffect(() => {
    const getJournalEntries = async () => {
      const response = await fetchJournalEntries();
      setJournalEntries(response.data);
    };
    getJournalEntries();
  }, []);

  return (
    <div>
      <JournalEntryForm setJournalEntries={setJournalEntries} />
      <ul>
        {journalEntries.map((entry) => (
          <li key={entry.id}>
            {entry.student} - {entry.date} <br />
            {entry.content} <br />
            Mentor Feedback: {entry.mentor_feedback || "N/A"} <br />
            Supervisor Feedback: {entry.supervisor_feedback || "N/A"}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default JournalEntryList;
