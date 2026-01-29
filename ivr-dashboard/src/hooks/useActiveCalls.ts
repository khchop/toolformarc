import { useQuery } from '@tanstack/react-query';

export interface ActiveCall {
  id: string;
  phoneNumber: string;
  status: 'inbound' | 'outbound' | 'completed';
  duration: number;
  timestamp: Date;
}

async function fetchActiveCalls(): Promise<ActiveCall[]> {
  const response = await fetch('/api/calls/active');
  if (!response.ok) {
    throw new Error('Failed to fetch active calls');
  }
  return response.json();
}

export function useActiveCalls() {
  return useQuery({
    queryKey: ['active-calls'],
    queryFn: fetchActiveCalls,
  });
}
