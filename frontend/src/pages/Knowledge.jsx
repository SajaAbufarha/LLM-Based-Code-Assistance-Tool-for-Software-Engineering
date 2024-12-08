import React from 'react';
import { Container, Row, Col } from '../components/Grid';
import shape from '../assets/img/pdf-02.svg';
import pdf1 from '/backend_pdfs/Refactoring-Improving-the-Design-of-Existing-Code-Addison-Wesley-Professional-1999.pdf';
import pdf2 from '/backend_pdfs/Software-Testing-A-Craftsman-s-Approach-Fourth-Edition-Paul-C-Jorgensen.pdf';

export default function Knowledge() {
    const pdfitems = [
        {
            img: shape,
            title: "Refactoring-Improving-the-Design-of-Existing-Code-Addison-Wesley-Professional-1999",
            size: "340 KB",
            file : pdf1,
        },
        {
            img: shape,
            title: "Software-Testing-A-Craftsman-s-Approach-Fourth-Edition-Paul-C-Jorgensen",
            size: "340 KB",
            file : pdf2, 
        },
    ]
    const downloadFile = (fileUrl, fileName) => {
        const link = document.createElement('a');
        link.href = fileUrl;
        link.setAttribute('download', fileName + '.pdf');
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
    };
    const downloadAll = () => {
        pdfitems.forEach((item) => {
          const link = document.createElement('a');
          link.href = item.file;
          link.setAttribute('download', item.title + ".pdf");
          document.body.appendChild(link);
          link.click();
          document.body.removeChild(link);
        });
      };
    return (
        <section className='knowledge'>
            <Container>
                <Row>
                    <Col xs={12} lg={6}>
                        <div className="pdf-wrapper">
                            <div className="pdf-top flex justify-between items-center mb-6">
                                <h1>Knowledge</h1>
                                <button onClick={downloadAll}>
                                    <svg width="24" height="25" viewBox="0 0 24 25" fill="none" xmlns="http://www.w3.org/2000/svg">
                                        <path d="M3.09477 10.5002C3.03217 10.9572 2.99976 11.4247 2.99976 11.9002C2.99976 17.2021 7.02919 21.5002 11.9998 21.5002C16.9703 21.5002 20.9998 17.2021 20.9998 11.9002C20.9998 11.4247 20.9673 10.9572 20.9047 10.5002" stroke="#E9FF04" strokeWidth="2" strokeLinecap="round" />
                                        <path d="M11.9998 13.5002V3.50024M11.9998 13.5002C11.2995 13.5002 9.99129 11.5059 9.49976 11.0002M11.9998 13.5002C12.7 13.5002 14.0082 11.5059 14.4998 11.0002" stroke="#E9FF04" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" />
                                    </svg>
                                </button>
                            </div>
                            <div className="pdf-items flex gap-[30px]">
                                {pdfitems.map((item, index) => (
                                    <div className="single-item" key={index}>
                                        <div className="pdf-img">
                                            <img src={item.img} alt="" />
                                        </div>
                                        <div className="pdf-info flex justify-between">
                                            <div>
                                                <h3>{item.title}</h3>
                                                <p>{item.size} <span>pdf</span></p>
                                            </div>

                                            <button onClick={() => downloadFile(item.file, item.title)}>
                                                <svg width="24" height="25" viewBox="0 0 24 25" fill="none" xmlns="http://www.w3.org/2000/svg">
                                                    <path d="M3.09477 10.5002C3.03217 10.9572 2.99976 11.4247 2.99976 11.9002C2.99976 17.2021 7.02919 21.5002 11.9998 21.5002C16.9703 21.5002 20.9998 17.2021 20.9998 11.9002C20.9998 11.4247 20.9673 10.9572 20.9047 10.5002" stroke="#E9FF04" stroke-width="2" stroke-linecap="round" />
                                                    <path d="M11.9998 13.5002V3.50024M11.9998 13.5002C11.2995 13.5002 9.99129 11.5059 9.49976 11.0002M11.9998 13.5002C12.7 13.5002 14.0082 11.5059 14.4998 11.0002" stroke="#E9FF04" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
                                                </svg>
                                            </button>
                                        </div>
                                    </div>
                                ))}
                            </div>
                        </div>
                    </Col>
                </Row>
            </Container>
        </section>
    )
}
