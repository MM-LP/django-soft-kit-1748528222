// FIXED: accordion.tsx with valid ARIA attribute and accessibility compliance

import { useState } from 'react'

type AccordionItem = {
  title: string
  content: string
}

const items: AccordionItem[] = [
  {
    title: 'What is your refund policy?',
    content: 'We offer a full refund within the first 30 days of your purchase if you are not satisfied.'
  },
  {
    title: 'Do you offer customer support?',
    content: 'Yes, we offer 24/7 customer support via chat and email.'
  },
  {
    title: 'Is this platform mobile-friendly?',
    content: 'Absolutely. Our design system ensures responsiveness across all screen sizes.'
  },
]

export default function Accordion() {
  const [activeIndex, setActiveIndex] = useState<number | null>(null)

  const toggle = (index: number) => {
    setActiveIndex(activeIndex === index ? null : index)
  }

  return (
    <div className="mx-auto max-w-2xl divide-y divide-slate-200 px-4 sm:px-6">
      {items.map((item, index) => {
        const isOpen = activeIndex === index
        return (
          <div key={index}>
            <button
              type="button"
              className="flex w-full items-center justify-between py-4 text-left text-lg font-medium text-slate-800 hover:text-indigo-600 focus:outline-none"
              onClick={() => toggle(index)}
              aria-expanded={isOpen ? 'true' : 'false'}
            >
              <span>{item.title}</span>
              <svg
                className={`h-5 w-5 transform transition-transform duration-200 ${isOpen ? 'rotate-180' : ''}`}
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 9l-7 7-7-7" />
              </svg>
            </button>
            <div
              className={`overflow-hidden transition-all duration-300 ease-in-out ${isOpen ? 'max-h-40' : 'max-h-0'}`}
            >
              <p className="pb-4 text-slate-600">{item.content}</p>
            </div>
          </div>
        )
      })}
    </div>
  )
}
