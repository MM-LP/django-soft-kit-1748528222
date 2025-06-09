"use client"

// FINAL REWRITE: testimonials-carousel.tsx with correct prop types and full responsiveness

import Image from 'next/image'
import { useRef, useEffect } from 'react'
import Testimonial from '@/components/testimonial'
import Logo from '@/public/images/logo.png'
import type { StaticImageData } from 'next/image'

const testimonials: {
  quote: string
  name: string
  title: string
  image: StaticImageData
  date: string
}[] = [
  {
    quote: 'This platform changed how we work entirely.',
    name: 'Alex Chen',
    title: 'Head of Product, NovaTech',
    image: Logo,
    date: '2024-11-10',
  },
  {
    quote: 'The integration was seamless and the support was fantastic.',
    name: 'Jamie Rivera',
    title: 'CTO, Skybound',
    image: Logo,
    date: '2024-11-12',
  },
  {
    quote: 'I can’t imagine going back to the old way of doing things.',
    name: 'Morgan Lee',
    title: 'CEO, QuantumSoft',
    image: Logo,
    date: '2024-11-15',
  },
]

export default function TestimonialsCarousel() {
  const scrollRef = useRef<HTMLDivElement>(null)

  useEffect(() => {
    const interval = setInterval(() => {
      if (scrollRef.current) {
        scrollRef.current.scrollLeft += 1
      }
    }, 30)
    return () => clearInterval(interval)
  }, [])

  return (
    <section className="relative bg-slate-50 py-20 overflow-hidden">
      {/* Glow background */}
      <div className="absolute left-1/2 top-1/2 h-[480px] w-[90vw] max-w-[480px] -translate-x-1/2 -translate-y-1/2 rounded-full bg-indigo-300 opacity-20 blur-[160px]" />

      {/* Scrollable row */}
      <div className="relative z-10 overflow-x-auto whitespace-nowrap px-4">
        <div ref={scrollRef} className="inline-flex gap-6">
          {testimonials.map((testimonial, index) => (
            <div key={index} className="w-[90vw] max-w-[22rem] shrink-0">
              <Testimonial
                testimonial={{
                  img: testimonial.image,
                  name: testimonial.name,
                  date: testimonial.date,
                  channel: testimonial.title,
                }}
              >
                {testimonial.quote}
              </Testimonial>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}
