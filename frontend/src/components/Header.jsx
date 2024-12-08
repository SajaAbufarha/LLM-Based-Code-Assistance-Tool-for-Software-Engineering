import { NavLink } from 'react-router-dom'
import { Container, Row, Col } from './Grid'
export default function Header() {
  return (
    <>
      <header className='heading'>
        <Container>
          <Row className="justify-center">
            <Col lg={6} className='flex justify-center'>
              <div className='heading-wrap max-w-max rounded-[20px] border border-[#393943] p-[14px_20px] md:p-[20px_24px] bg-[#2A2A36] flex items-center justify-between gap-5 sm:gap-8 md:gap-[56px]'>
                <NavLink className='text-white text-base md:text-[18px] font-medium leading-[1.6] opacity-70' to='/'>Home</NavLink>
                <NavLink className='text-white text-base md:text-[18px] font-medium leading-[1.6] opacity-70' to='/codeAssistance'>Code Assistance</NavLink>
                <NavLink className='text-white text-base md:text-[18px] font-medium leading-[1.6] opacity-70' to='/knowledge'>Knowledge</NavLink>
              </div>
            </Col>
          </Row>
        </Container>
      </header>
    </>
  )
}
