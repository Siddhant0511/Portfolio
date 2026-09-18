import { useEffect, useRef, type ComponentPropsWithoutRef } from "react"
import { animate, useInView, useMotionValue, useReducedMotion } from "motion/react"

import { cn } from "@/lib/utils"

interface NumberTickerProps extends ComponentPropsWithoutRef<"span"> {
  value: number
  startValue?: number
  direction?: "up" | "down"
  delay?: number
  decimalPlaces?: number
  /** Locale grouping; en-IN renders 10,52,714 style. */
  locale?: string
  /** Seconds. A tween, not a spring, so the count is guaranteed to land by then. */
  duration?: number
}

export function NumberTicker({
  value,
  startValue = 0,
  direction = "up",
  delay = 0,
  className,
  decimalPlaces = 0,
  locale = "en-US",
  duration = 0.9,
  ...props
}: NumberTickerProps) {
  const ref = useRef<HTMLSpanElement>(null)
  const motionValue = useMotionValue(direction === "down" ? value : startValue)
  const isInView = useInView(ref, { once: true, margin: "0px" })
  const reduceMotion = useReducedMotion()
  const format = (n: number) =>
    Intl.NumberFormat(locale, {
      minimumFractionDigits: decimalPlaces,
      maximumFractionDigits: decimalPlaces,
    }).format(Number(n.toFixed(decimalPlaces)))

  useEffect(() => {
    if (reduceMotion) {
      if (ref.current) ref.current.textContent = format(value)
      return
    }
    if (!isInView) return

    const controls = animate(motionValue, direction === "down" ? startValue : value, {
      duration,
      delay,
      ease: [0.16, 1, 0.3, 1],
    })
    return () => controls.stop()
  }, [motionValue, isInView, delay, duration, value, direction, startValue, reduceMotion])

  useEffect(
    () =>
      motionValue.on("change", (latest) => {
        if (ref.current) {
          ref.current.textContent = format(latest)
        }
      }),
    [motionValue, decimalPlaces]
  )

  return (
    <span
      ref={ref}
      className={cn(
        "inline-block tabular-nums",
        className
      )}
      {...props}
    >
      {format(startValue)}
    </span>
  )
}
