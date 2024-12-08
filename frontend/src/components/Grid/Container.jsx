
export default function Container({children, className='', fluid=false}) {
  return (
    <div className={`${fluid?'w-full':'container'} px-3 ${className}`} >
        {children}
    </div>
  )
}
