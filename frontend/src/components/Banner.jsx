import React from 'react'
import { Container, Row, Col } from './Grid'
import shape from '../assets/img/banner-shape.png'
import { Link } from 'react-router-dom'
export default function Banner() {
  const bannerCard = [
    {
      icon: `<svg width="26" height="26" viewBox="0 0 26 26" fill="none" xmlns="http://www.w3.org/2000/svg">
                <g opacity="0.8">
                  <path d="M5.36127 17.1C4.87225 16.0255 4.59961 14.8302 4.59961 13.5706C4.59961 8.8924 8.36042 5.09998 12.9996 5.09998C17.6389 5.09998 21.3996 8.8924 21.3996 13.5706C21.3996 14.8302 21.1269 16.0255 20.6379 17.1" stroke="white" stroke-width="1.5" stroke-linecap="round"/>
                  <path d="M13 1.5V2.7" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                  <path d="M24.9998 13.5H23.7998" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                  <path d="M2.2 13.5H1" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                  <path d="M15.9753 21.897C17.1781 21.46 17.6605 20.2235 17.7962 18.9798C17.8367 18.6082 17.5645 18.3 17.2312 18.3L8.78473 18.3003C8.43997 18.3003 8.1631 18.6289 8.20426 19.0133C8.33718 20.2547 8.67265 21.1615 9.94733 21.897M15.9753 21.897C15.9753 21.897 10.1572 21.897 9.94733 21.897ZM15.9753 21.897C15.8306 24.4976 15.1619 25.5275 12.987 25.4987C10.6606 25.5469 10.1254 24.2739 9.94733 21.897" fill="white"/>
                </g>
              </svg>`,
      title: 'Code Refactoring',
      des: 'Auto-optimize code for clarity and speed.',
      color: '#9D65ED',
    },
    {
      icon: `<svg width="24" height="25" viewBox="0 0 24 25" fill="none" xmlns="http://www.w3.org/2000/svg">
                <g opacity="0.8">
                  <path d="M8 10.6667L12.1232 6.54344C13.2481 5.41858 13.8105 4.85614 14.4312 4.40314C15.7047 3.4737 17.1818 2.86187 18.7395 2.61858C19.4988 2.5 20.2942 2.5 21.885 2.5C21.9681 2.5 22 2.53812 22 2.61504C22 4.20584 22 5.00125 21.8814 5.76046C21.6381 7.31818 21.0263 8.79527 20.0969 10.0688C19.6439 10.6895 19.0814 11.2519 17.9566 12.3768L13.8333 16.5" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                  <path d="M10.341 8.59838C8.63808 8.59838 6.49778 8.23765 4.9043 8.89769C3.73671 9.38132 2.87754 10.5012 2 11.3787L5.30597 12.7955C6.18208 13.171 5.64651 14.2766 5.50147 15.0018C5.33985 15.8099 5.34886 15.8397 5.93158 16.4224L8.07758 18.5684C8.6603 19.1511 8.69008 19.1602 9.49816 18.9985C10.2234 18.8535 11.329 18.3179 11.7044 19.194L13.1213 22.5C13.9988 21.6225 15.1187 20.7633 15.6023 19.5957C16.2624 18.0022 15.9016 15.8619 15.9016 14.159" stroke="white" stroke-width="1.5" stroke-linejoin="round"/>
                  <path d="M12 20.5L11 21.5" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                  <path d="M4 12.5L3 13.5" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                  <path d="M15 4.57996C16.2 4.75996 17.46 5.23996 18.1614 5.95996C19.0576 6.75211 19.68 7.81996 19.92 9.49996" stroke="white" stroke-width="1.5" stroke-linecap="square"/>
                  <path d="M17.94 6.56006L16.5 8.00006" stroke="white" stroke-width="1.5" stroke-linecap="round"/>
                </g>
             </svg>`,
      title: 'Test Case Generation',
      des: 'Create edge cases and boost test coverage fast.',
      color: '#E9FE09',
    },
    {
      icon: `<svg width="24" height="25" viewBox="0 0 24 25" fill="none" xmlns="http://www.w3.org/2000/svg">
                <g opacity="0.8">
                  <path d="M8 10.6667L12.1232 6.54344C13.2481 5.41858 13.8105 4.85614 14.4312 4.40314C15.7047 3.4737 17.1818 2.86187 18.7395 2.61858C19.4988 2.5 20.2942 2.5 21.885 2.5C21.9681 2.5 22 2.53812 22 2.61504C22 4.20584 22 5.00125 21.8814 5.76046C21.6381 7.31818 21.0263 8.79527 20.0969 10.0688C19.6439 10.6895 19.0814 11.2519 17.9566 12.3768L13.8333 16.5" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                  <path d="M10.341 8.59838C8.63808 8.59838 6.49778 8.23765 4.9043 8.89769C3.73671 9.38132 2.87754 10.5012 2 11.3787L5.30597 12.7955C6.18208 13.171 5.64651 14.2766 5.50147 15.0018C5.33985 15.8099 5.34886 15.8397 5.93158 16.4224L8.07758 18.5684C8.6603 19.1511 8.69008 19.1602 9.49816 18.9985C10.2234 18.8535 11.329 18.3179 11.7044 19.194L13.1213 22.5C13.9988 21.6225 15.1187 20.7633 15.6023 19.5957C16.2624 18.0022 15.9016 15.8619 15.9016 14.159" stroke="white" stroke-width="1.5" stroke-linejoin="round"/>
                  <path d="M12 20.5L11 21.5" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                  <path d="M4 12.5L3 13.5" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                  <path d="M15 4.57996C16.2 4.75996 17.46 5.23996 18.1614 5.95996C19.0576 6.75211 19.68 7.81996 19.92 9.49996" stroke="white" stroke-width="1.5" stroke-linecap="square"/>
                  <path d="M17.94 6.56006L16.5 8.00006" stroke="white" stroke-width="1.5" stroke-linecap="round"/>
                </g>
            </svg>`,
      title: 'Contextual Assistance',
      des: 'Use AI to decode complex code patterns.',
      color: '#9D65EB',
    },
  ]
  return (
    <div className="banner relative z-[1]"> 
      <img src={shape} alt="" className="shape absolute z-[-1] top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2" />
      <Container>
        <Row className='justify-center'>
          <Col xs={12} className='lg:!p-0'>
            <div className="banner-content">
              <h1 className='mb-2 md:mb-4 lg:mb-5 text-white text-center  font-medium leading-[1.2]'>LLM Based <span className='text-[#7A7A7F]'> Code Assistance <span className='italic'>Tool</span></span></h1>
              <p className='mb-4 lg:mb-6 text-[#69696C] text-center text-base md:text-[18px] font-normal !leading-[1.6]'>Streamline coding, auto-generate test cases, and access instant, contextual assistance with ease.</p>
              <div className="flex items-center justify-center">
              <Link to="/codeAssistance" className="btn flex items-center justify-center gap-1">
                  Get Started
                  <svg width="24" height="24" viewBox="0 0 24 24" fill="none">
                    <path d="M14 10L6 18" stroke="white" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" />
                    <path d="M15.8384 5.10643L14.2418 5.25158C11.6551 5.48673 10.3618 5.60431 10.0575 6.44499C9.75299 7.28567 10.6714 8.20398 12.508 10.0406L13.9594 11.492C15.796 13.3286 16.7144 14.247 17.555 13.9425C18.3957 13.6382 18.5133 12.3449 18.7484 9.75815L18.8936 8.1616C19.0351 6.60414 19.106 5.8254 18.6403 5.35973C18.1746 4.89406 17.3958 4.96485 15.8384 5.10643Z" fill="white" />
                  </svg>
                </Link>
              </div>
            </div>
          </Col>
        </Row>
        <Row className=''>
          {bannerCard.map((item, index) => (
            <Col xs={12} md={6} xl={4} className='banner-cards flex items-center'>
              <div className="banner-card rounded-[20px] w-full" key={index}>
                <div className="inner p-4 md:p-6 lg:p-7 xl:p-8 flex items-center gap-3 md:gap-4 lg:gap-5 xl:gap-6">
                  <span className={`h-[70px] w-1 rounded-2xl`} style={{ backgroundColor: item.color }}></span>
                  <div className="">
                    <div className="flex items-center gap-2 lg:gap-3 mb-2 lg:mb-3 xl:mb-4">
                      <div className="icon" dangerouslySetInnerHTML={{ __html: item.icon }}></div>
                      <h4 className='text-white text-lg md:text-xl lg:text-[22px] font-medium !leading-[1.4] opacity-80'>{item.title} </h4>
                    </div>
                    <p className='opacity-50 text-white text-base font-normal !leading-[1.4]'>{item.des}</p>
                  </div>
                </div>
              </div>
            </Col>
          ))}
        </Row>
      </Container>
    </div>
  )
}
