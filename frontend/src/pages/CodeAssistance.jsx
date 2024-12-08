import React, { useState } from 'react';
import { Container, Row, Col } from '../components/Grid';
import Editor from 'react-simple-code-editor';
import { highlight, languages } from 'prismjs/components/prism-core';
import 'prismjs/components/prism-clike';
import 'prismjs/components/prism-javascript';
import 'prismjs/components/prism-python';
import 'prismjs/themes/prism-tomorrow.css';
import Dropdown from 'react-dropdown';
import 'react-dropdown/style.css';

export default function CodeAssistance() {
    const [code, setCode] = useState(``);
    const [taskType, setTaskType] = useState('Refactor Code');
    const [language, setLanguage] = useState('python');
    const [response, setResponse] = useState(null);
    const [context, setContext] = useState('');

    const taskTypes = ['Refactor Code', 'Generate Tests'];
    const languageOptions = [
        { value: 'javascript', label: 'JavaScript' },
        { value: 'python', label: 'Python' },
        { value: 'clike', label: 'C-like' },
    ];

    const handleSubmit = async () => {
        try {
            const res = await fetch('http://127.0.0.1:5000/api/generate', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    code: code,
                    task: taskType,
                    language: language,
                    context: context,
                }),
            });

            if (!res.ok) {
                throw new Error(`Error: ${res.statusText}`);
            }

            const data = await res.json();
            let parsedResponse;

            if (data.response && typeof data.response === 'string') {
                parsedResponse = JSON.parse(data.response);
            } else if (data.code && data.explanation) {
                parsedResponse = data;
            } else {
                parsedResponse = { error: 'Unexpected response format.' };
            }

            setResponse(parsedResponse);
        } catch (error) {
            console.error(error);
            setResponse({ error: 'An error occurred. Please try again.' });
        }
    };

    const getLineNumbers = (code) => {
        return code ? code.split('\n').map((_, index) => index + 1).join('\n') : '1';
    };

    return (
        <section className="code pt-4">
            <Container>
                <Row>
                    <Col xs={12} lg={6}>
                        <div className="code-left relative">
                            <div className="dropdown-area lg:flex justify-between gap-7 mb-9">
                                <div className="task-type item">
                                    <h3>Task Type</h3>
                                    <Dropdown
                                        options={taskTypes}
                                        onChange={(e) => setTaskType(e.value)}
                                        value={taskType}
                                        placeholder="Select a task type"
                                    />
                                </div>
                                <div className="language item">
                                    <h3>Programming Language</h3>
                                    <Dropdown
                                        options={languageOptions}
                                        onChange={(e) => setLanguage(e.value)}
                                        value={languageOptions.find(opt => opt.value === language)}
                                        placeholder="Select a language"
                                    />
                                </div>
                            </div>
                            <div className="editor-area relative ps-[20px]">
                                <div
                                    className="linenumber absolute left-0 z-10"
                                    style={{
                                        backgroundColor: '#2A2A36',
                                        color: '#888',
                                        padding: '10px 5px',
                                        textAlign: 'right',
                                        fontFamily: '"Fira code", "Fira Mono", monospace',
                                        fontSize: 14,
                                        userSelect: 'none',
                                        lineHeight: '1.6',
                                        width: '20px',
                                    }}
                                >
                                    {getLineNumbers(code)}
                                </div>
                                <Editor
                                    value={code}
                                    onValueChange={(code) => setCode(code)}
                                    highlight={(code) => highlight(code, languages[language], language)}
                                    padding={10}
                                    style={{
                                        fontFamily: '"Fira code", "Fira Mono", monospace',
                                        fontSize: 14,
                                        backgroundColor: '#2A2A36',
                                        color: '#fff',
                                        minHeight: '300px',
                                        width: '100%',
                                        lineHeight: '1.6',
                                    }}
                                />
                            </div>
                            <button
                                className="bg-[#B991E4] p-1 rounded-md w-[56] h-[56] absolute bottom-4 right-8"
                                onClick={handleSubmit}
                            >
                                Submit
                            </button>
                        </div>
                        </Col>
                        <Col xs={12} lg={6}>
                        <div className="result-area">
                            
                            <div className="editor-area">
                                
                                    <Editor
                                        value={response?.code || response?.test || 'No code generated.'}
                                        onValueChange={() => {}} 
                                        highlight={(code) => highlight(code, languages[language], language)}
                                        padding={10}
                                        style={{
                                            fontFamily: '"Fira code", "Fira Mono", monospace',
                                            fontSize: 14,
                                            backgroundColor: '#2A2A36',
                                            color: '#fff',
                                            minHeight: '300px',
                                            width: '100%',
                                            lineHeight: '1.6',
                                        }}
                                    />
                                </div>
                            </div>
                        </Col>
                    </Row>
                <Row>
                    <Col xs={12}>
                        <div className="explanation mt-8">
                            <p
                                style={{
                                    color: '#fff', 
                                    backgroundColor: '#2A2A36',
                                    padding: '10px',
                                    borderRadius: '5px',
                                    fontFamily: '"Fira code", "Fira Mono", monospace',
                                    fontSize: 14,
                                    lineHeight: '1.6',
                                }}
                            >
                                {response?.explanation || 'No explanation provided.'}
                            </p>
                        </div>
                    </Col>
                </Row>
            </Container>
        </section>
    );
}
